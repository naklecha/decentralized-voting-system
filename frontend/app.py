from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form['name']
        bio = request.form['biometric']
        print(name,bio)
    return render_template('verification.html')

if __name__ == '__main__':
	app.run(host="127.0.0.1" ,port=4000, debug = True)