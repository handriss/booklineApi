from flask import Flask, request, jsonify

from app.minimum_price import MinimumPriceService
from app.validator import ValidatorService

app = Flask(__name__)
minimum_price_service = MinimumPriceService()
validator_service = ValidatorService()


@app.route("/", methods=['GET'])
def get_index():
    response = {
        'message': 'Method not allowed.'
    }
    return jsonify(response)


@app.route("/healthcheck", methods=['GET'])
def get_index():
    response = {
        'success': True
    }
    return jsonify(response)


@app.route("/", methods=['POST'])
def index():

    if request.json:
        book_data = request.json
        target_url = minimum_price_service.build_url(book_data.get("author"), book_data.get("title"))
        minimum_price = minimum_price_service.send_request(target_url)

        response = {
            'author': book_data.get('author'),
            'title': book_data.get('title'),
            'minimumPrice': minimum_price
        }
        return jsonify(response)


if __name__ == '__main__':
    app.run()
