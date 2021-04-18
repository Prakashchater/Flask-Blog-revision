from flask import Flask, render_template, url_for, redirect
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
from flask_bootstrap import Bootstrap
import csv
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "qwertyuiop"
Bootstrap(app)


class cafeForm(FlaskForm):
    cafe = StringField(label='cafes', validators=[DataRequired()])
    location = StringField(label='Cafe location', validators=[DataRequired(), URL()])
    open = StringField(label='Opening Time e.g. 8am', validators=[DataRequired()])
    close = StringField(label='Closing Time e.g. 11pm', validators=[DataRequired()])
    coffee = SelectField(label='Coffee rating',
                         choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
                         validators=[DataRequired()])
    wifi = SelectField(label='Wifi Strength Rating',
                       choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
                       validators=[DataRequired()])
    power = SelectField(label='Power Supply Rating',
                        choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
                        validators=[DataRequired()])

    submit = SubmitField(label='Submit')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = cafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', mode='a', encoding="utf8") as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee.data},"
                           f"{form.wifi.data},"
                           f"{form.power.data}"
                           )
        return redirect(url_for('cafes'))
    return render_template("add.html", form=form)

@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)



if __name__ == '__main__':
    app.run(debug=True)