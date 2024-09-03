from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/product-search', methods=['GET'])
def product_search():
    url = 'https://real-time-flipkart-api.p.rapidapi.com/product-search'

    querystring = {
        "q": "new balance 2002",
        "page": "1",
        "sort_by": "popularity"
    }
    
    headers = {
        'x-rapidapi-host': 'real-time-flipkart-api.p.rapidapi.com',
        'x-rapidapi-key': '5474778fb9msh8b56259111e5167p1293bejsn5fa61ff373d1'
    }
    
    try:
        response = requests.get(url, headers=headers, params=querystring)
        
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({
                'statusCode': response.status_code,
                'body': f"Failed to fetch data. Status code: {response.status_code}, Response: {response.text}"
            }), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({
            'statusCode': 500,
            'body': f"An error occurred: {e}"
        }), 500

if __name__ == "__main__":
    app.run(debug=True)

def lambda_handler(event, context):
    from aws_lambda_wsgi import lambda_handler as wsgi_handler
    return wsgi_handler(app, event, context)
