from flask import Flask, request

from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from opentelemetry.trace import get_tracer_provider, set_tracer_provider
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

set_tracer_provider(TracerProvider())

url_traces = 'http://localhost:4317'
otlp_exporter_traces = OTLPSpanExporter(endpoint=url_traces)
tracer_provider = get_tracer_provider()
tracer_provider.add_span_processor(span_processor=BatchSpanProcessor(span_exporter=otlp_exporter_traces))

def request_hook(span, environ):
    if span and span.is_recording():
        span.set_attribute("custom_user_attribute_from_request_hook", "some-value")

def response_hook(span, status, resresponse_header):
    if span and span.is_recording():
        span.set_attribute("custom_user_attribute_from_response_hook", "some-value")

app = Flask(__name__)
FlaskInstrumentor().instrument_app(
    app=app,
    request_hook=request_hook, 
    response_hook=response_hook
)
    
print(app)
# instrumentor.instrument_app(app, excluded_urls="/server_request")

@app.route("/server_request")
def server_request():
    print(request.args.get("param"))
    return "served"

if __name__ == "__main__":
    app.run(port=8082)