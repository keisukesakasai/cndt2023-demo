import logging

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
    
    return "9999999999"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)