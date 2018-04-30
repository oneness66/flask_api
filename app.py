from flask import Flask, jsonify,json
from quotes import funny_quotes
import random
import requests

app = Flask(__name__)

@app.route("/api/phonenumber")
def phonenumbervalidation():
	response = requests.get('http://apilayer.net/api/validate?access_key=81f511599e67f381ac1ff12743ca4753&number=9618467907&country_code=IN&format=1')
    return json.dumps(response.text)


if __name__ == "__main__":
	app.run(debug=True)