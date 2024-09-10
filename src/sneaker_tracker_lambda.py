import requests
import os
from flask import Flask, request, jsonify
from api_service.flipkart_api_service import product_search as flipkart_ps
from api_service.lazada_api_service import product_search as lazada_ps

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    param = request.args.get('word')
    res1 = flipkart_ps(param)
    res2 = lazada_ps(param)
    combined_results = {
        "flipkart_results": res1,
        "lazada_results": res2
    }

    return res1

if __name__ == '__main__':
    app.run(debug=True)
  