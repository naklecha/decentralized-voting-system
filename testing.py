from web3 import Web3
rpc = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(rpc))
contract_addr = '0x8fDd21C593c5693788E0248b4C86bB66375f8dA7'
abi = '[{"constant":true,"inputs":[],"name":"candidatesCount","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"candidates","outputs":[{"name":"id","type":"uint256"},{"name":"name","type":"string"},{"name":"voteCount","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"voters","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_candidateId","type":"uint256"}],"name":"votedEvent","type":"event"},{"constant":false,"inputs":[{"name":"_candidateId","type":"uint256"}],"name":"vote","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'

# ----------------------------------------------------------->

# Send ETH from account1 to account2
'''
account1 = '0xB0BE5EFDe83490f0d8fC64120461660098AE7599'
account1_key = '25d9479cd21fb800522f8e0c74513f0730f7afac9f3ac7a23d8ad69b7103be52'
account2 = '0xe7043cb8c5E6EEc2057297760EcACa0293847d54'

transaction = {
            'nonce'     : web3.eth.getTransactionCount(account1),
            'to'        : account2,
            'value'     : web3.toWei(1,'ether'),
            'gas'       : 2000000,
            'gasPrice'  : web3.toWei('50','gwei')
}
signed_tx = web3.eth.account.signTransaction(transaction, account1_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
'''

# ----------------------------------------------------------->

#Make vote from account3
'''
account3 = "0x35A3c8A48fb58B1d418D62c752Eeb4DA36128564"
account3_key = "571f96e9291b198b7e024ab950d5868dbdc6b6137ee30bddb51ff450fa7591ce"

contract = web3.eth.contract(address=contract_addr, abi=abi)
transaction  = contract.functions.vote(2).buildTransaction()
transaction['nonce'] = web3.eth.getTransactionCount(account3)

signed_tx = web3.eth.account.signTransaction(transaction, account3_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
'''

# ----------------------------------------------------------->

# Check number of votes a candidate has recieved

election = web3.eth.contract(address=contract_addr, abi=abi)
print(election.__dict__)
for i in range(election.caller().candidatesCount()):    
    candidates  = election.caller().candidates(i+1)
    print(candidates)

# ----------------------------------------------------------->



