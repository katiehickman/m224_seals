# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


@app.route('/aboutus/')
def aboutus():
    return render_template("aboutus.html")

@app.route('/minilab/')
def minilab():
    return render_template("minilab.html")

@app.route('/binary/')
def binary():
    return render_template("binary.html")

@app.route('/greetkatie', methods=['GET', 'POST'])
def greetkatie():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greetkatie.html", name=name)
    # starting and empty input default
    return render_template("greetkatie.html", name="Katie")

@app.route('/greetshreya', methods=['GET', 'POST'])
def greetshreya():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greetshreya.html", name=name)
    # starting and empty input default
    return render_template("greetshreya.html", name="Shreya")

@app.route('/greetderek', methods=['GET', 'POST'])
def greetderek():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greetderek.html", name=name)
    # starting and empty input default
    return render_template("greetderek.html", name="Derek")

@app.route('/greetkian', methods=['GET', 'POST'])
def greetkian():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greetkian.html", name=name)
    # starting and empty input default
    return render_template("greetkian.html", name="Kian")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
