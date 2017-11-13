from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['POST'])
def json():

    if request.json:
        book_data = request.json
        return "Author: " + book_data.get("author") + " Title: " + book_data.get("title")


if __name__ == '__main__':
    app.run()
