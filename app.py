from flask import Flask, request, jsonify

from service.minimum_price import MinimumPriceService
from service.validator import ValidatorService

app = Flask(__name__)
minimum_price_service = MinimumPriceService()
validator_service = ValidatorService()


@app.route("/healthcheck", methods=['GET'])
def get_index():
    response = {
        'success': True
    }
    return jsonify(response)

@app.route("/example", methods=['GET'])
def get_example():
    response = {'example': 'is working'}
    return jsonify(response)

@app.route("/", methods=['POST'])
def index():

    if request.json:
        book_data = request.json

        if not validator_service.validate(book_data):
            response = {
                'message': 'Invalid request'
            }
        else:
            target_url = minimum_price_service.build_url(book_data.get("author"), book_data.get("title"))
            minimum_price = minimum_price_service.send_request(target_url)

            response = {
                'requestData': {
                    'author': book_data.get('author'),
                    'title': book_data.get('title'),
                },
                'responseData': {
                    'minimumPrice': minimum_price
                }
        }
    else:
        response = {
            'message': 'Content-type should be in JSON'
        }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
