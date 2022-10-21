from flask import Flask, request, render_template, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def index():
    session.clear()
    return render_template("front page.html")


@app.route("/signin", methods=["POST"])
def signin():
    inputPOST = request.form["ID"]
    passwordPOST = request.form["password"]

    if inputPOST == "test" and passwordPOST == "test":
        session["ID"] = os.urandom(12)
        return redirect(url_for("member"))

    elif inputPOST != "test" or passwordPOST != "test":

        if inputPOST == "" or passwordPOST == "":
            session["fail"] = os.urandom(12)
            return redirect(url_for("error", message="請輸入帳號、密碼"))

        session["fail"] = os.urandom(12)
        return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))


@app.route("/member")
def member():
    if "ID" in session:
        return render_template("success.html")
    return redirect(url_for("index"))


@app.route("/error")
def error():
    if "fail" in session:
        errorTEXT = request.args.get("message")
        return render_template("fail.html", errorTEXT=errorTEXT)
    return redirect(url_for("index"))


@app.route("/signout")
def signout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(port=3000)
