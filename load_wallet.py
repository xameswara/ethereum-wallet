# load_wallet.py
from eth_account import Account

# Fungsi untuk memuat wallet dari private key
def load_wallet(private_key_hex):
    account = Account.from_key(private_key_hex)
    return account.privateKey.hex(), account.address

# Memuat wallet dari private key yang ada
private_key_hex = 'YOUR_PRIVATE_KEY'  # Ganti dengan private key-mu
private_key, address = load_wallet(private_key_hex)

# Menampilkan informasi wallet
print(f"Private Key: {private_key}")
print(f"Address: {address}")
