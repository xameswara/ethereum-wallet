# check_balance.py
from web3 import Web3

# Menghubungkan ke node Ethereum
web3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"))

# Address wallet yang ingin diperiksa
address = 'YOUR_WALLET_ADDRESS'

# Memeriksa saldo
balance = web3.fromWei(web3.eth.get_balance(address), 'ether')

print(f"Address: {address}")
print(f"Balance: {balance} ETH")
