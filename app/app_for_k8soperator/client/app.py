import requests
from flask import Flask
import time
import os
import logging
import redis

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def hello_world():
    url = os.getenv('SERVER_URL', 'http://localhost:8090/')
    url_go_server = os.getenv('SERVER_URL_GO_SERVER', 'http://localhost:8090/')
    url_nodejs_server = os.getenv('SERVER_URL_NODEJS_SERVER', 'http://localhost:3000/')
    logger.info("url: %s", url)

    # 受け取ったデータを Redis に保存
    redis_password = os.getenv('REDIS_PASSWORD', 'bEbppdLTA6')
    client = redis.StrictRedis(host=os.getenv('REDIS_URL', 'redis-master'), port=6379, password=redis_password, decode_responses=True)
    # For Local
    # client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)
    client.get("my-key")
    logger.info(f"Rdis Key: {time.time()}")
    
    response = send_request(url)
    
    response_go_server = send_request_go_server(url_go_server)
    
    response_nodejs_server = send_request_node_js(url_nodejs_server)
    
    return response + " + " + response_go_server + " + " + response_nodejs_server
    
def send_request(url):
    try:
        response = requests.get(url)
        response_text = response.text
        logger.info(f"Response from server: {response_text}")
        
        return response_text

    except requests.exceptions.ConnectionError:
        logger.warning("Server is not available. Skipping this request.")    
        
        return None
    
def send_request_go_server(url_go_server):
    try:
        response = requests.get(url_go_server)
        response_text = response.text
        logger.info(f"Response from server: {response_text}")
        
        return response_text

    except requests.exceptions.ConnectionError:
        logger.warning("Server is not available. Skipping this request.")    
        
        return None    
    
def send_request_node_js(url_nodejs_server):
    try:
        response = requests.get(url_nodejs_server)
        response_text = response.text
        logger.info(f"Response from server: {response_text}")
        
        return response_text

    except requests.exceptions.ConnectionError:
        logger.warning("Server is not available. Skipping this request.")    
        
        return None    
            
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)