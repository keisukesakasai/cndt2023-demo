import os,time,logging,sqlite3

import redis
import psycopg2
import requests
from flask import Flask, request

app = Flask(__name__)

# Logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Handler
@app.route('/get', methods=['POST'])
def main():
    # Get Data
    pref = request.data.decode()
    logger.info(f"Pref.: {pref}")
    
    # Query Cache ( Redis )
    cache = query_cache(pref)
    logger.info(f"Population in Cache: {cache}")

    if cache is not None:
        population = cache
    else:
        # Query DB
        region = query_db(pref)
        logger.info(f"Region: {region}")
    
        # Request Backend Service
        population = send_request(pref, region)
    
        # Set Cache ( Redis )
        set_cache(region, population)

    return population

def query_cache(key):
    client = redis.StrictRedis(host="localhost", port=6379)
    key_cache = client.get(key)
    
    return key_cache

def set_cache(region, population):
    client = redis.StrictRedis(host="localhost", port=6379)
    client.set(region, population, ex=60)

def query_db(key):
    conn = psycopg2.connect("postgresql://postgres:password@localhost/postgres")
    cur = conn.cursor()

    cur.execute("SELECT region FROM prefectures WHERE prefecture_name = %s", (key,))
    result_region = cur.fetchall()[0][0]

    cur.close()
    conn.close()
    
    return result_region

def send_request(pref, region):
    if region == "東日本": 
        _url = os.getenv('EASTERN_API_URL', 'http://localhost:8089/call_eastern_api')
        url = _url + f"?pref={pref}"
    elif region == "西日本": 
        _url = os.getenv('WESTERN_API_URL', 'http://localhost:8090/call_western_api')
        url = _url + f"?pref={pref}"
    try: 
        logger.info(f"URL: {url}")
        response = requests.get(url)
        population = response.text
        logger.info(f"Response from server: {population}")
        
        return population
    except requests.exceptions.ConnectionError:
        logger.warning("Server is not available. Skipping this request.")

        return None

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)