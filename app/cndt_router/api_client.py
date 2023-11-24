import os
import requests
from logger import setup_logger

logger = setup_logger()

def send_request_to_backend(prefecture_name, region):
    if region == "Eastern":
        base_url = os.getenv('CNDT_ROUTER_EASTERN_API_URL', 'http://localhost:8089/call_eastern_api')
    elif region == "Western":
        base_url = os.getenv('CNDT_ROUTER_WESTERN_API_URL', 'http://localhost:8090/call_western_api')
    url = f"{base_url}?pref={prefecture_name}"
    logger.info(f'URL: {url}')
    
    try:
        response = requests.get(url)

        return response.text

    except requests.exceptions.ConnectionError as e:
        logger.warning(f"Connection error: {e}")
        
        return None