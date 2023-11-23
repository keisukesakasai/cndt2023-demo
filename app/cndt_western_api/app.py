import base64,logging

import mysql.connector
from pymemcache.client import base
from flask import Flask, request

app = Flask(__name__)

# Logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Handler
@app.route('/call_western_api', methods=['GET'])
def main():
    # Get Data
    pref = request.args.get('pref')
    logger.info(f"Pref.: {pref}")
    
    # Query Cache ( Memcache )
    cache = query_cache(pref)
    logger.info(f"Population in Cache: {cache}")
    
    if cache != None:
        population = cache
    else:
        # Query DB
        print(pref, type(pref))
        population = query_db(pref)
        logger.info(f"Popuration: {population}")

        # Set Cache ( Memcache )
        set_cache(pref, population)

    return population

def query_cache(key):
    client = base.Client(('localhost', 11211))
    key_cache = client.get(key)
    
    if key_cache is not None:
        return key_cache
    return None

def set_cache(pref, population):
    client = base.Client(('localhost', 11211))
    client.set(pref, population, expire=60)

def query_db(pref):
    config = {
        'user': 'western',
        'password': 'password',
        'host': '127.0.0.1',
        'database': 'western',
        'raise_on_warnings': True,
        'port': 3307,
    }
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    logger.info(f"Pref.: {pref}")
    query = "SELECT population FROM population WHERE prefecture = %s"
    cursor.execute(query, (pref,))    

    result = cursor.fetchone()
    return str(result[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)