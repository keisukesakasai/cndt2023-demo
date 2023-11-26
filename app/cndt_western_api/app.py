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

url = 'http://localhost:5080/api/default/traces'
headers = {"Authorization": "Basic cm9vdEBleGFtcGxlLmNvbTpDb21wbGV4cGFzcyMxMjMK"}
otlp_exporter = OTLPSpanExporter(endpoint=url, headers=headers)
span_processor = BatchSpanProcessor(otlp_exporter)
tracer_provider.add_span_processor(span_processor=BatchSpanProcessor(span_exporter=otlp_exporter))
tracer_provider.add_span_processor(span_processor=SimpleSpanProcessor(span_exporter=ConsoleSpanExporter()))
trace.set_tracer_provider(tracer_provider)

# CNDT WESTERN API Main Hander: From Prefecture Name To Population.
@app.route('/call_western_api', methods=['GET'])
def main():
    with tracer.start_as_current_span(
    "/call_eastern_api",
    context=extract(request.headers),
    kind=trace.SpanKind.SERVER,
    # attributes=collect_request_attributes(request.environ),
    ):    
        # Get Data
        pref = request.args.get('pref')
        logger.info(f"リクエスト受信: {pref}")
        
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