import time,os
from flask import Flask, request
import logging
import redis

from opentelemetry import trace
tracer = trace.get_tracer(__name__)

app = Flask(__name__)

# Logger Config.
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def hello_world():
    method = request.method
    url = request.url
    logger.info("Received request: %s %s", method, url)
    
    # 受け取ったデータを Redis に保存
    redis_password = os.getenv('REDIS_PASSWORD', 'bEbppdLTA6')
    client = redis.StrictRedis(host=os.getenv('REDIS_URL', 'redis-master'), port=6379, password=redis_password, decode_responses=True)
    # For Local
    # client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
    client.set(f"my key", method)
    logger.info(f"Rdis Key: {time.time()}")
    
    with tracer.start_as_current_span(
        "自動計装だけど、一個だけ Span を挟んでみるムーブ",
        kind=trace.SpanKind.CLIENT) as span:

        time.sleep(0.1)
        span.set_attribute("my_attribute", "foo")    
    
    # 受け取ったデータを Redis に保存
    client = redis.StrictRedis(host=os.getenv('REDIS_URL', 'redis-master'), port=6379, password=redis_password, decode_responses=True)
    # For Local
    # client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
    client.get("my-key")
    logger.info(f"Rdis Key: {time.time()}")
                
    return 'Hello from Flask Server'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)