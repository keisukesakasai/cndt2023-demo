import os
import mysql.connector
from pymemcache.client import base
from logger import setup_logger

from opentelemetry import trace

logger = setup_logger()
tracer = trace.get_tracer(__name__)

# Get Population from Memchache.
def get_population_from_cache(key):
    with tracer.start_as_current_span(
    "get_population_from_cache",
    kind=trace.SpanKind.INTERNAL,
    # attributes=collect_request_attributes(request.environ),
    ):
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
    with tracer.start_as_current_span(
    "set_population_to_cache",
    kind=trace.SpanKind.INTERNAL,
    # attributes=collect_request_attributes(request.environ),
    ):
        memcache_host = os.getenv('CNDT_WESTERN_API_MEMCACHE_HOST', 'localhost')
        memcache_port = int(os.getenv('CNDT_WESTERN_API_MEMCACHE_PORT', 11211))
        expire_time = int(os.getenv('CNDT_WESTERN_API_MEMCACHE_EXPIRE_TIME', 60))

        client = base.Client((memcache_host, memcache_port))
        client.set(pref, population, expire=expire_time)
        logger.info(f"Cache 設定 ( TTL: {expire_time} 秒 ): {pref}:{population}")

# Get Population from MySQL.
def get_population_from_db(pref):
    with tracer.start_as_current_span(
    "get_population_from_db",
    kind=trace.SpanKind.INTERNAL,
    # attributes=collect_request_attributes(request.environ),
    ):    
        config = {
            'user': os.getenv('CNDT_WESTERN_API_DB_USER', 'western'),
            'password': os.getenv('CNDT_WESTERN_API_DB_PASSWOR', 'password'),
            'host': os.getenv('CNDT_WESTERN_API_DB_HOST', '127.0.0.1'),
            'database': os.getenv('CNDT_WESTERN_API_DB_NAME', 'western'),
            'port': os.getenv('CNDT_WESTERN_API_DB_PORT', 3307),
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