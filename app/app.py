from flask import Flask, request
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)

def assert_arg_count(argc, args):
    assert len(args) == argc, ("args needs to be exactly %d was %d" % (argc, len(args)))

def update(updated, matrix, args):
    assert_arg_count(4, args)
    x = args[0]-1; y = args[1]-1; z = args[2]-1
    w = args[3]
    matrix[x][y][z] = w
    updated.add((x, y, z))

def query(updated, matrix, args):
    assert_arg_count(6, args)

    def find_in_bounds(updated, args):
        (x1, y1, z1, x2, y2, z2) = args

        coords = []
        for (x, y, z) in updated:
            if x >= (x1-1) and x < x2 and y >= (y1-1) and y < y2 and z >= (z1-1) and z < z2:
                coords.append((x, y, z))
        return coords

    coords = find_in_bounds(updated, args)

    sum = 0
    for (x, y, z) in coords:
        sum += matrix[x][y][z]

    print (sum)
    return sum

def exec_command(line, updated, matrix):
    def to_int(args):
        return [int(x) for x in args]

    args = to_int(line.split(' ')[1:])
    value = 0
    if line.startswith('UPDATE'):
        update(updated, matrix, args)
    elif line.startswith('QUERY'):
        value = query(updated, matrix, args)
    else:
        assert (False)
    return value

def create_matrix(n):
    return [[[0 for k in range(n)] for j in range(n)] for i in range(n)]

def results(tests, n, commands):
    test_cases = tests

    resp = []
    for case in range(0, test_cases):
        updated = set()
        matrix = create_matrix(n)
        for c in commands:
            res = exec_command(c, updated, matrix)
            resp.append(res)
    return resp

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