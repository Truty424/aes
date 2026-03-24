import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7

key_aes = os.urandom(32)
iv = os.urandom(16)

key_chacha = os.urandom(32)
nonce_chacha = os.urandom(16)

# Encrypt with AES-CBC + PKCS7
cipher_enc = Cipher(algorithms.AES(key_aes), modes.CBC(iv))
padder = PKCS7(algorithms.AES.block_size).padder()
padded = padder.update(b"a secret message") + padder.finalize()
ct = cipher_enc.encryptor().update(padded) + cipher_enc.encryptor().finalize()

# Decrypt with ChaCha20
cipher_dec = Cipher(algorithms.ChaCha20(key_chacha, nonce_chacha), modes.CBC(iv))
res = cipher_dec.decryptor().update(ct) + cipher_dec.decryptor().finalize()

print(res)
