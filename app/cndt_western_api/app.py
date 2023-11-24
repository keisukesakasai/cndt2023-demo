import os
from flask import Flask, request
from database import get_population_from_cache, set_population_to_cache, get_population_from_db
from logger import setup_logger

app = Flask(__name__)
logger = setup_logger()

# CNDT WESTERN API Main Hander: From Prefecture Name To Population.
@app.route('/call_western_api', methods=['GET'])
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
    host, port = os.getenv('CNDT_WESTERN_API_HOST', '0.0.0.0'), os.getenv('CNDT_WESTERN_API_PORT', 8090)
    app.run(host=host, port=port)