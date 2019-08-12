from flask import Flask, jsonify, abort, make_response, request, url_for
from flask import render_template, redirect
import json
import re
import requests
import hashlib
import os
from web3 import Web3

rpc = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(rpc))
contract_addr = '0x8fDd21C593c5693788E0248b4C86bB66375f8dA7'
abi = '[{"constant":true,"inputs":[],"name":"candidatesCount","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"candidates","outputs":[{"name":"id","type":"uint256"},{"name":"name","type":"string"},{"name":"voteCount","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"voters","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_candidateId","type":"uint256"}],"name":"votedEvent","type":"event"},{"constant":false,"inputs":[{"name":"_candidateId","type":"uint256"}],"name":"vote","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'

app = Flask(__name__)

accounts = eval(open('accounts').read())

privatekeys = eval(open('private_keys').read())

voted = []

@app.route("/" , methods=['POST'])
def home():
    try:
        data = eval(request.data) # {"aadhaarID":int(),"candidateID":int()}
        aid = int(data["aadhaarID"])-1
        if(aid in voted):
            return "Already voted",200
        cid = int(data["candidateID"])
        acc = accounts[aid]
        pvt = privatekeys[aid]
        contract = web3.eth.contract(address=contract_addr, abi=abi)
        transaction  = contract.functions.vote(cid).buildTransaction()
        transaction['nonce'] = web3.eth.getTransactionCount(acc)

        signed_tx = web3.eth.account.signTransaction(transaction, pvt)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        voted.append(aid)
        return "Vote successfully casted",200
    except:
        return "Error processing",500

@app.route("/results" , methods=['GET'])
def count():
    try:
        res = []
        election = web3.eth.contract(address=contract_addr, abi=abi)
        for i in range(election.caller().candidatesCount()):    
            res.append(election.caller().candidates(i+1))
        return json.dumps(res),200
    except:
        return "Error processing",500

@app.route("/number_of_users" , methods=['GET'])
def number_of_users(): 
    try:
        return str(len(accounts)),200
    except:
        return "Error processing",500

@app.route("/candidates_list" , methods=['GET'])
def candidates_list():
    try:
        res = []
        election = web3.eth.contract(address=contract_addr, abi=abi)
        for i in range(election.caller().candidatesCount()):    
            res.append(election.caller().candidates(i+1)[1]) #name
        return json.dumps(res),200
    except:
        return "Error processing",500

if __name__ == '__main__':
	app.run(host="127.0.0.1" ,port=3000, debug = True)