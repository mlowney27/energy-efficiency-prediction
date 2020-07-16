from flask import Flask, request
from predict import predict_building, validate_input
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def predict():
    """
    If post, make a prediction. If get, print statement about how to make requests
    :return:
    """
    if request.method == 'POST':
        data = request.get_json(force=True)
        if validate_input(data):
            prediction = predict_building(data)
            output = "Heating load: {}  Cooling load: {}".format(prediction[0][0], [prediction[0][1]])
            return output
        else:
            return "Request data malformatted"

    return 'send building data as a json post request {X1: 10.2, ... X8: 5}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)