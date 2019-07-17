from flask import Flask, request, jsonify
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    data = request.form
    data = data.to_dict(flat=False)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)