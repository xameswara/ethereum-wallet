# create_wallet.py
from eth_utils import to_checksum_address
import os
from eth_keys import keys

# Fungsi untuk membuat dompet baru
def create_wallet():
    private_key = os.urandom(32)
    pk = keys.PrivateKey(private_key)
    public_key = pk.public_key
    address = to_checksum_address(public_key.to_address())
    return private_key.hex(), public_key, address

# Membuat wallet
private_key, public_key, address = create_wallet()

# Menampilkan hasil
print(f"Private Key: {private_key}")
print(f"Public Key: {public_key}")
print(f"Address: {address}")
