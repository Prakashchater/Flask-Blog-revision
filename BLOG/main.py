from flask import Flask, render_template, request
import requests
from smtplib import SMTP

username = "chaterprakash@gmail.com"
password = "pcchater@160997"

posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_message(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_send=True)
    return render_template("contact.html", msg_send=False)


def send_message(name, email, phone, message):
    message = f"Subject: New Message \n\n name:{name}\n phone_no:{phone} \n email-id: {email} \n message:{message}"
    with SMTP("smtp.gmail.com") as sm:
        sm.starttls()
        sm.login(user=username, password=password)
        sm.sendmail(from_addr=username, to_addrs=username,msg=message)




if __name__ == "__main__":
    app.run(debug=True)
