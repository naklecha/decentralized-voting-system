from flask import Flask, render_template, flash, request, session, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import requests;
import json;

backend_addr = "https://election-backend.azurewebsites.net/"

app = Flask(__name__)
app.secret_key = 'i love white chocolate'

@app.route("/", methods=['GET', 'POST'])
def home():
    return redirect(url_for('verify'))

@app.route("/results", methods=['GET'])
def results():
    try:
        resp = requests.get(backend_addr+'results')
        if(resp.status_code!=200):
            return render_template('confirmation.html',message=resp.text),resp.status_code
        result = eval(resp.text)
        print(result)
        result.sort(reverse=True,key=lambda x: x[2])
        return render_template('results.html',result=result)
    except:
        return render_template('confirmation.html',message="Error processing"),500
    
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
        return render_template('confirmation.html',message="Error processing"),500

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
                return render_template('confirmation.html',message=resp.text,code=resp.status_code),resp.status_code
            return render_template('vote.html',candidates1=candidates1,candidates2=candidates2),200
        else:
            return redirect(url_for('verify'))
    except:
        return render_template('confirmation.html',message="Error processing"),500

if __name__ == '__main__':
	app.run(host="127.0.0.1" ,port=4000, debug = True)