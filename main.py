from flask import redirect, request, render_template, url_for, Flask
from fib import fb

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/result", methods=["POST"])
def result():
    u_input1 = request.form.get("num1")
    u2=request.form.get("num2)
    return render_template("result.html", sum_ = 34)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
