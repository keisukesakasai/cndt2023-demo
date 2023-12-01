import requests
from flask import Flask
import os
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def hello_world():
    url_go_server = os.getenv('SERVER_URL_GO_SERVER', 'http://localhost:8090/')
    logger.info("url: %s", url_go_server)

    response_go_server = send_request_go_server(url_go_server)
    
    return response_go_server
    
def send_request_go_server(url_go_server):
    try:
        response = requests.get(url_go_server)
        response_text = response.text
        logger.info(f"Response from server: {response_text}")
        
        return response_text

    except requests.exceptions.ConnectionError:
        logger.warning("Server is not available. Skipping this request.")    
        
        return None    
            
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)