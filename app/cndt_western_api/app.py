import os, time, random
from flask import Flask, request
from database import get_population_from_cache, set_population_to_cache, get_population_from_db
from logger import setup_logger

app = Flask(__name__)
logger = setup_logger()

# === OTel Configuration.
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
    SimpleSpanProcessor,
)
from opentelemetry.propagate import extract
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

resource = Resource(attributes={
    "service.name": "CNDT_WESTERN_API"
})

tracer_provider = TracerProvider(resource=resource)
tracer = trace.get_tracer(__name__)

url_traces = 'http://localhost:5080/api/default/traces'
headers = {"Authorization": "Basic cm9vdEBleGFtcGxlLmNvbTpDb21wbGV4cGFzcyMxMjMK"}
otlp_exporter_traces = OTLPSpanExporter(endpoint=url_traces, headers=headers)

tracer_provider.add_span_processor(span_processor=BatchSpanProcessor(span_exporter=otlp_exporter_traces))
# tracer_provider.add_span_processor(span_processor=SimpleSpanProcessor(span_exporter=ConsoleSpanExporter()))
trace.set_tracer_provider(tracer_provider)

# === OTel COnfiguration. ( Metrics )
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics.export import (
    ConsoleMetricExporter,
    PeriodicExportingMetricReader,
)

url_metrics = 'http://localhost:5080/api/default/v1/metrics'
otlp_reader = PeriodicExportingMetricReader(OTLPMetricExporter(endpoint=url_metrics, headers=headers))
# console_reader = PeriodicExportingMetricReader(ConsoleMetricExporter())
# metrics_provider = MeterProvider(metric_readers=[otlp_reader, console_reader], resource=resource)
metrics_provider = MeterProvider(metric_readers=[otlp_reader], resource=resource)
metrics.set_meter_provider(metrics_provider)

meter = metrics.get_meter(__name__)

# Custom Metrics ( Updown Counter )
request_counter = meter.create_up_down_counter(
    name="http_requests_by_prefecture",
    description="Number of HTTP Request of 都道府県",
    unit="1",
)

# CNDT WESTERN API Main Hander: From Prefecture Name To Population.
@app.route('/call_western_api', methods=['GET'])
def main():
    with tracer.start_as_current_span(
    "/call_eastern_api",
    context=extract(request.headers),
    kind=trace.SpanKind.SERVER,
    ):    
        # Get Data
        pref = request.args.get('pref')
        logger.info(f"リクエスト受信: {pref}")
        # Counter Pref.
        request_counter.add(1, {"prefecture": pref})        
        
        # Get Cache ( Memcache ).
        cache = get_population_from_cache(pref)
        
        if cache != None:
            population = cache
        else:
            # Query DB ( MySQL ).
            population = get_population_from_db(pref)

            # Set Cache ( Memcache )
            set_population_to_cache(pref, population)
        
        # Random Sleep.
        time.sleep(random.uniform(0, 1))

        return population

if __name__ == '__main__':
    host, port = os.getenv('CNDT_WESTERN_API_HOST', '0.0.0.0'), os.getenv('CNDT_WESTERN_API_PORT', 8090)
    app.run(host=host, port=port)