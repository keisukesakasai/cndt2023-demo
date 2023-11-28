from flask import Flask
import logging
import mysql.connector

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/")
def main():
    result = get_population_from_db("Okinawa-Ken")
    logger.info(f"result = {result}")

    return result

# Get Population from MySQL.
def get_population_from_db(pref):
    config = {
        'user': 'western',
        'password': 'password',
        'host': '127.0.0.1',
        'database': 'western',
        'port':  3307,
        'raise_on_warnings': True,
    }
    
    try: 
        cnx = mysql.connector.connect(**config)
        print(f"cnx は {cnx}")
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

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)