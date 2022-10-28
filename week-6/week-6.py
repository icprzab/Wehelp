from flask import Flask, request, render_template, redirect, url_for, session
import os
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="website"
)

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def index():
    session.clear()
    return render_template("front page.html")


@app.route("/signup", methods=["POST"])
def signup():
    mycursor = db.cursor()
    input_ID = request.form["new_ID"]
    query = "SELECT * FROM member WHERE username = %s"
    mycursor.execute(query, (input_ID,))
    myresult = mycursor.fetchone()

    if myresult == None:
        input_name = request.form["new_name"]
        input_ID = request.form["new_ID"]
        input_password = request.form["new_password"]
        query2 = "INSERT INTO member(name, username, password) VALUES(%s,%s,%s)"
        mycursor.execute(query2, (input_name, input_ID, input_password,))
        db.commit()
        return redirect(url_for("index"))
    elif myresult != None:
        session["fail"] = os.urandom(12)
        return redirect(url_for("error", message="帳號已經被註冊"))


@app.route("/signin", methods=["POST"])
def signin():
    mycursor2 = db.cursor()
    input_post = request.form["ID"]
    password_post = request.form["password"]
    query3 = "SELECT id,username,password FROM member WHERE username = %s AND password = %s "
    mycursor2.execute(query3, (input_post, password_post,))
    myresult2 = mycursor2.fetchone()

    if input_post == str(myresult2[1]) and password_post == str(myresult2[2]):
        session["ID"] = os.urandom(12)
        session["member_name"] = input_post
        session["member_id"] = myresult2[0]
        return redirect(url_for("member"))

    else:
        if input_post == "" or password_post == "":
            session["fail"] = os.urandom(12)
            return redirect(url_for("error", message="請輸入帳號、密碼"))

        session["fail"] = os.urandom(12)
        return redirect(url_for("error", message="帳號、或密碼輸入錯誤"))


@app.route("/member")
def member():
    if "ID" in session:
        member_name = session["member_name"]
        mycursor3 = db.cursor()
        mycursor3.execute(
            "SELECT member.username, message.content FROM member INNER JOIN message ON member.id=message.member_id ORDER BY message.id ASC")
        myresult3 = mycursor3.fetchall()

        return render_template("success.html", member_name=member_name, myresult3=myresult3)
    return redirect(url_for("index"))


@app.route("/message", methods=["POST"])
def message():
    mycursor4 = db.cursor()
    message_content = request.form["message_content"]
    member_id = session["member_id"]
    if message_content != "":
        query4 = "INSERT INTO message(member_id,content) VALUES(%s,%s)"
        mycursor4.execute(query4, (member_id, message_content))
        db.commit()
        return redirect(url_for("member"))
    return redirect(url_for("member"))


@app.route("/error")
def error():
    if "fail" in session:
        error_text = request.args.get("message")
        return render_template("fail.html", error_text=error_text)
    return redirect(url_for("index"))


@app.route("/signout")
def signout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.debug = True
    app.run(port=3000)
