from flask import Flask, render_template, flash, request, session
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)
app.secret_key = 'i love white chocolate'

@app.route("/verify", methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        name = request.form['aid']
        bio = request.form['biometric']
        session['verified'] = True
        print(name,bio)
    return render_template('verification.html')

@app.route("/vote", methods=['GET', 'POST'])
def vote():
    if request.method == 'POST':
        print("in post")
    return render_template('vote.html',candidates1=['c1','c2','c3'],candidates2=['c4','c5','c6'])

if __name__ == '__main__':
	app.run(host="127.0.0.1" ,port=4000, debug = True)