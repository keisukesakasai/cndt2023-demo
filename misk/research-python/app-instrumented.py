from random import randint
from flask import Flask, request
import logging

# === OTel Configuration.
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
    SimpleSpanProcessor,
)
from opentelemetry.sdk.resources import Resource

resource = Resource(attributes={
    "service.name": "CNDT_EASTERN_API"
})

tracer_provider = TracerProvider(resource=resource)
tracer = trace.get_tracer(__name__)

tracer_provider.add_span_processor(span_processor=SimpleSpanProcessor(span_exporter=ConsoleSpanExporter()))
trace.set_tracer_provider(tracer_provider)

# === Auto Instrument
from opentelemetry.instrumentation.flask import FlaskInstrumentor

app = Flask(__name__)
# FlaskInstrumentor().instrument_app(app)
FlaskInstrumentor().instrument_app(app)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/rolldice")
def roll_dice():
    player = request.args.get('player', default=None, type=str)
    result = str(roll())
    if player:
        logger.warning(f"{player} is rolling the dice: {result}")
    else:
        logger.warning("Anonymous player is rolling the dice: %s", result)
    return result

def roll():
    return randint(1, 6)

if __name__ == "__main__":
    app.run()