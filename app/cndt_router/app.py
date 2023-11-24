import os
from flask import Flask, request
from database import get_population_from_cache, set_population_to_cache, get_region_from_db
from api_client import send_request_to_backend
from logger import setup_logger

app = Flask(__name__)
logger = setup_logger()

# CNDT ROUTER Main Hander: From Prefecture Name To Population.
@app.route('/get', methods=['POST'])
def main():
    # Get Request Data.
    pref = request.data.decode()
    logger.info(f"リクエスト受信: {pref}")
    
    # Get Cache ( Redis ).
    cache = get_population_from_cache(pref)

    if cache is not None:
        population = cache.decode('utf-8')
    else:
        # Query DB ( Postgres ).
        region = get_region_from_db(pref)
        if region not in ['Eastern', 'Western']: return "Invalid Prefecture Name"            
    
        # Request Backend Service ( HTTP GET Request ).
        population = send_request_to_backend(pref, region)
        if population is None: return "Connection Error"

    population_million = int(population) / 10**4
    
    # Set Cache ( Redis ).
    set_population_to_cache(pref, population)

    return f"{pref} の人口は {population_million} 万人です"

if __name__ == '__main__':
    host, port = os.getenv('CNDT_ROUTER_HOST', '0.0.0.0'), os.getenv('CNDT_ROUTER_PORT', 8080)
    app.run(host=host, port=port)