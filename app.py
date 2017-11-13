from flask import Flask, request

from app.minimum_price import MinimumPriceService
from app.validator import ValidatorService

app = Flask(__name__)
minimum_price_service = MinimumPriceService()
validator_service = ValidatorService()


@app.route("/", methods=['POST'])
def index():

    if request.json:
        book_data = request.json
        target_url = minimum_price_service.build_url(book_data.get("author"), book_data.get("title"))
        minimum_price_service.send_request(target_url)
        return 'cica'


if __name__ == '__main__':
    app.run(debug=True)
