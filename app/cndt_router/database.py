import os
import redis
import psycopg2

# Get Population from Redis.
def get_population_from_cache(prefecture_name):
    client = redis.StrictRedis(host=os.getenv('REDIS_HOST', 'localhost'), port=os.getenv('REDIS_PORT', 6379))

    return client.get(prefecture_name)

# Set Population from Redis ( expire = 60 Sec. ).
def set_population_to_cache(prefecture_name, population):
    client = redis.StrictRedis(host=os.getenv('CNDT_ROUTER_REDIS_HOST', 'localhost'), port=os.getenv('REDIS_PORT', 6379))
    client.set(prefecture_name, population, ex=60)

# Get Region ( Eastern or Western ) from Postgres.    
def get_region_from_db(prefecture_name):
    conn = psycopg2.connect(os.getenv('CNDT_ROUTER_DATABASE_URL', "postgresql://postgres:password@localhost/postgres"))
    cur = conn.cursor()

    cur.execute("SELECT region FROM prefectures WHERE prefecture_name = %s", (prefecture_name,))
    region = cur.fetchone()

    cur.close()
    conn.close()
    
    return region[0] if region else None    