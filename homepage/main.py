from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/guess/<name>')
def guess(name):
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(url=age_url).json()
    age_data = age_response["age"]
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(url=gender_url).json()
    gender_data = gender_response["gender"]
    return render_template("guess.html", name=name, age=age_data, gender=gender_data)

if __name__ == "__main__":
    app.run(debug=True)