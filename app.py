from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/fibonacci/<int:fib_get>', methods=['GET'])

def fib(fib_get):   # return Fibonacci series up to fib_get
    result = []
    a, b = 0, 1
    while b < fib_get:
        result.append(b)
        a, b = b, a+b
    return jsonify({'fibonacci': result})

if __name__ == '__main__':
    app.run(debug=False)
