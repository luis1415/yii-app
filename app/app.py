from flask import Flask, request
from werkzeug.datastructures import ImmutableMultiDict
from cube import *


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate():
    data = request.form
    data = data.to_dict(flat=False)
    tests = int(data['tests'][0])
    n = int(data['matrixDimension'][0])
    print(tests, n)
    commands = []
    for i, v in data.items(): 
        if v[0].startswith('QUERY') or v[0].startswith('UPDATE'):
            commands.append(v[0])

    results_ = results(tests, n, commands)
    results_ = [i for i in results_ if i !=0]
    return str(results_)


if __name__ == "__main__":
    app.run(debug=True)