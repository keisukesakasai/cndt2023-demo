import os
from flask import Flask, request
from database import get_population_from_cache, set_population_to_cache, get_population_from_db
from logger import setup_logger

logger = setup_logger()

# === OTel Configuration.
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
    SimpleSpanProcessor,
)
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.trace import get_tracer_provider, set_tracer_provider

resource = Resource(attributes={
    "service.name": "CNDT-EASTER-API"
})

tracer_provider = TracerProvider(resource=resource)
tracer = trace.get_tracer(__name__)

otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
span_processor = BatchSpanProcessor(otlp_exporter)
tracer_provider.add_span_processor(span_processor=BatchSpanProcessor(span_exporter=otlp_exporter))
tracer_provider.add_span_processor(span_processor=SimpleSpanProcessor(span_exporter=ConsoleSpanExporter()))
trace.set_tracer_provider(tracer_provider)

# === Auto Instrument
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.pymemcache import PymemcacheInstrumentor
from opentelemetry.instrumentation.mysql import MySQLInstrumentor

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
PymemcacheInstrumentor().instrument()
MySQLInstrumentor().instrument()

# CNDT EASTERN API Main Hander: From Prefecture Name To Population.
@app.route('/call_eastern_api', methods=['GET'])
def main():
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

    return population

if __name__ == '__main__':
    host, port = os.getenv('CNDT_EASTERN_API_HOST', '0.0.0.0'), os.getenv('CNDT_EASTERN_API_PORT', 8089)
    app.run(host=host, port=port)