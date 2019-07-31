from web3 import Web3
rpc = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(rpc))
contract_addr = '0x9251237cD41BaA7739A10848861C09617F3Fa9CA'

# ----------------------------------------------------------->

# Send ETH from account1 to account2
'''
account1 = '0x9Ff7534EdA51D84E5d1f96099327Ce0d95822463'
account1_key = '8b369fdde0264bf69cc0452516a2f0b1d98da7b34dd1fe6d9d97157628d6e00b'
account2 = '0x44579E04222292f11177efE2450f3dFB6f843B18'

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
account3 = "0x1b373b788f743068430a71f0Aed3BAB15c27D8e4"
account3_key = "a8e8be42577507a37c821dab459ea8f7a69cb1198a55d898c41df5ea4392aadf"

contract = web3.eth.contract(address=contract_addr, abi='[{"constant":true,"inputs":[],"name":"candidatesCount","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function","signature":"0x2d35a8a2"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"candidates","outputs":[{"name":"id","type":"uint256"},{"name":"name","type":"string"},{"name":"voteCount","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function","signature":"0x3477ee2e"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"voters","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function","signature":"0xa3ec138d"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor","signature":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_candidateId","type":"uint256"}],"name":"votedEvent","type":"event","signature":"0xfff3c900d938d21d0990d786e819f29b8d05c1ef587b462b939609625b684b16"},{"constant":false,"inputs":[{"name":"_candidateId","type":"uint256"}],"name":"vote","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function","signature":"0x0121b93f"}]')

transaction  = contract.functions.vote(2).buildTransaction()
transaction['nonce'] = web3.eth.getTransactionCount(account3)

signed_tx = web3.eth.account.signTransaction(transaction, account3_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
'''

# ----------------------------------------------------------->

# Check number of votes a candidate has recieved
election = web3.eth.contract(address=contract_addr, abi='[{"constant":true,"inputs":[],"name":"candidatesCount","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function","signature":"0x2d35a8a2"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"candidates","outputs":[{"name":"id","type":"uint256"},{"name":"name","type":"string"},{"name":"voteCount","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function","signature":"0x3477ee2e"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"voters","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function","signature":"0xa3ec138d"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor","signature":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_candidateId","type":"uint256"}],"name":"votedEvent","type":"event","signature":"0xfff3c900d938d21d0990d786e819f29b8d05c1ef587b462b939609625b684b16"},{"constant":false,"inputs":[{"name":"_candidateId","type":"uint256"}],"name":"vote","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function","signature":"0x0121b93f"}]')
candidates  = election.call().candidates(1)
print(candidates)
candidates  = election.call().candidates(2)
print(candidates)

# ----------------------------------------------------------->



