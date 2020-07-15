from flask import Flask, request
app = Flask(__name__)

#TODO use uwsgi server or something better than flask default
@app.route('/', methods=['POST', 'GET'])
def predict():
    """
    If post, just return json data. If get, print statement
    :return:
    """
    if request.method == 'POST':
        data = request.get_json(force=True)
        return data

    return 'send building data as a json file'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')