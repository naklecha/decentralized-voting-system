from flask import Flask, render_template, flash, request, session, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import requests;
import json;

backend_addr = "http://localhost:3000/"

app = Flask(__name__)
app.secret_key = 'i love white chocolate'

@app.route("/", methods=['GET', 'POST'])
def home():
    return redirect(url_for('verify'))
    
@app.route("/verify", methods=['GET', 'POST'])
def verify():
    try:
        if request.method == 'POST':
            aid = request.form['aid']
            bio = request.form['biometric']
            resp = requests.get(backend_addr+'number_of_users')
            number_of_accounts = int(resp.text)
            if(bio == 'yes' and aid.isdigit() and int(aid)<=number_of_accounts):
                session['verified'] = True
                session['aid'] = int(aid)
                return redirect(url_for('vote'))
        return render_template('verification.html')
    except:
        return "Error processing",500

@app.route("/vote", methods=['GET', 'POST'])
def vote():
    try:
        if('verified' in session):
            resp = requests.get(backend_addr+'candidates_list')
            candidates = eval(resp.text)
            print(candidates)
            candidates1 = candidates[:int(len(candidates)/2)]
            candidates2 = candidates[int(len(candidates)/2):]
            if request.method == 'POST':
                aid = session['aid']
                session.pop('verified')
                session.pop('aid')
                candidate = request.form['candidate']
                cid = candidates.index(candidate)+1
                print(cid)
                resp = requests.post(backend_addr,json.dumps({'aadhaarID':aid,'candidateID':cid}))
                print(resp)
                return resp.text, 200
            return render_template('vote.html',candidates1=candidates1,candidates2=candidates2)
        else:
            return redirect(url_for('verify'))
    except:
        return "Error processing",500

if __name__ == '__main__':
	app.run(host="127.0.0.1" ,port=4000, debug = True)