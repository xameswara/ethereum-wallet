# send_transaction.py
from web3 import Web3
from eth_account import Account

# Menghubungkan ke node Ethereum
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Ganti dengan URL Infura-mu
web3 = Web3(Web3.HTTPProvider(infura_url))

# Fungsi untuk mengirim transaksi
def send_transaction(private_key, to_address, value_in_ether):
    account = Account.from_key(private_key)
    tx = {
        'nonce': web3.eth.getTransactionCount(account.address),
        'to': to_address,
        'value': web3.toWei(value_in_ether, 'ether'),
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei'),
        'chainId': 1
    }
    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return tx_hash

# Data transaksi
private_key = 'YOUR_PRIVATE_KEY'  # Ganti dengan private key-mu
to_address = 'RECEIVER_WALLET_ADDRESS'  # Ganti dengan address tujuan
value_in_ether = 0.01  # Jumlah ether yang dikirim

tx_hash = send_transaction(private_key, to_address, value_in_ether)

print(f"Transaction Hash: {web3.toHex(tx_hash)}")
