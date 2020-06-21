
from flask import Flask, request, render_template, redirect


# Setting app to be
app = Flask("__name__")

# Homepage of the application
@app.route("/")
def index():
    return render_template("index.html")


# Speed test route handling
@app.route('/testing', methods=["GET", "POST"])
def testing():
    if request.method == "POST":
        timing = request.form.get('timing')
        return render_template("testing.html", timing=timing)
    else:
        return render_template("testing.html", timing=60)


# Flash typing page
@app.route("/quicktyping")
def flashtyping():
    return render_template("quicktyping.html")

