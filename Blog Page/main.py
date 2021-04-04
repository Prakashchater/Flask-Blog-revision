from flask import Flask, render_template
from post import Post
import requests

response = requests.get(url="https://api.npoint.io/5abcca6f4e39b4955965").json()
posts = []
for post in response:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    posts.append(post_obj)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_post=posts)

@app.route('/blog/<int:index>')
def get_blog(index):
    req_post = None
    for blog_post in posts:
        if blog_post.id == index:
            req_post = blog_post
    return render_template("post.html", post=req_post)


if __name__ == "__main__":
    app.run(debug=True)
