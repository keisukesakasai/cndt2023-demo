import os
import redis
import psycopg2
from logger import setup_logger

logger = setup_logger()

# Get Population from Redis.
def get_population_from_cache(prefecture_name):
    client = redis.StrictRedis(host=os.getenv('CNDT_ROUTER_REDIS_HOST', 'localhost'), port=os.getenv('CNDT_ROUTER_REDIS_PORT', 6379))

    cache = client.get(prefecture_name)
    logger.info(f"Cache 取得: {cache}")

    return cache

# Set Population from Redis ( default expire time = 30 Sec. ).
def set_population_to_cache(pref, population):
    client = redis.StrictRedis(host=os.getenv('CNDT_ROUTER_REDIS_HOST', 'localhost'), port=os.getenv('REDIS_PORT', 6379))
    expire_time = os.getenv('CNDT_ROUTER_CACHE_EXPIRE_TIME', 30)
    
    client.set(pref, population, ex=expire_time)
    logger.info(f"Cache 設定 ( TTL: {expire_time} 秒 ): {pref}:{population}")

# Get Region ( Eastern or Western ) from Postgres.    
def get_region_from_db(prefecture_name):
    conn = psycopg2.connect(os.getenv('CNDT_ROUTER_DATABASE_URL', "postgresql://postgres:password@localhost/postgres"))
    cur = conn.cursor()

    cur.execute("SELECT region FROM prefectures WHERE prefecture_name = %s", (prefecture_name,))
    region = cur.fetchone()[0]
    logger.info(f"DB からデータ取得: {region}")

    cur.close()
    conn.close()
    
    return region if region else None    