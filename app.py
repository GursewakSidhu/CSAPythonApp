from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    args = request.args
    return render_template("index.html", userid=args)

@app.route("/hi/")
def who():
    return "who are you?"

@app.route("/<username>")
def user(username):
    return f"Hi there, {username}!"


@app.route("/login/", methods=["POST","GET"])
def login():
    if request.method == "POST":
        usr = request.form["nm"]
        return redirect(url_for("user", username=usr))
    else:
        return render_template("login.html")

@app.route("/admin/")
def admin():
    return redirect(url_for("user", username="Admin!"))

if __name__ == "__main__":
    app.run(debug=True)