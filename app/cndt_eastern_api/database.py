import os
import mysql.connector
from pymemcache.client import base
from logger import setup_logger

logger = setup_logger()

# Get Population from Memchache.
def get_population_from_cache(key):
    memcache_host = os.getenv('CNDT_WESTERN_API_MEMCACHE_HOST', 'localhost')
    memcache_port = int(os.getenv('CNDT_WESTERN_API_MEMCACHE_PORT', 11211))

    client = base.Client((memcache_host, memcache_port))
    cache = client.get(key)
    logger.info(f"Cache 取得: {cache}")
    
    if cache is None:
        return None
    
    return cache

# Set Population from Redis ( default expire time = 60 Sec. ).
def set_population_to_cache(pref, population):
    memcache_host = os.getenv('CNDT_EASTERN_API_MEMCACHE_HOST', 'localhost')
    memcache_port = int(os.getenv('CNDT_EASTERN_API_MEMCACHE_PORT', 11211))
    expire_time = int(os.getenv('CNDT_EASTERN_API_MEMCACHE_EXPIRE_TIME', 60))

    client = base.Client((memcache_host, memcache_port))
    client.set(pref, population, expire=expire_time)
    logger.info(f"Cache 設定 ( TTL: {expire_time} 秒 ): {pref}:{population}")

# Get Population from MySQL.
def get_population_from_db(pref):
    config = {
        'user': os.getenv('CNDT_EASTERN_API_DB_USER', 'eastern'),
        'password': os.getenv('CNDT_EASTERN_API_DB_PASSWOR', 'password'),
        'host': os.getenv('CNDT_EASTERN_API_DB_HOST', '127.0.0.1'),
        'database': os.getenv('CNDT_EASTERN_API_DB_NAME', 'eastern'),
        'port': os.getenv('CNDT_EASTERN_API_DB_PORT', 3306),
        'raise_on_warnings': True,
    }
    
    try: 
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        query = "SELECT population FROM population WHERE prefecture = %s"
        cursor.execute(query, (pref,))    
        
        result = cursor.fetchone()

        population = str(result[0]) if result else "Not Found"
        logger.info(f"DB からデータ取得: {population}")
    finally:
        cursor.close()
        cnx.close()
        
    return population