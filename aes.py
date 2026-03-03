import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7

key_enc = os.urandom(32)
key_dec = os.urandom(16)
iv = os.urandom(16)

cipher_enc = Cipher(algorithms.AES(key_enc), modes.CBC(iv))
padder = PKCS7(algorithms.AES.block_size).padder()
padded = padder.update(b"a secret message") + padder.finalize()
ct = cipher_enc.encryptor().update(padded) + cipher_enc.encryptor().finalize()

cipher_dec = Cipher(algorithms.AES(key_dec), modes.CBC(iv))
padded_res = cipher_dec.decryptor().update(ct) + cipher_dec.decryptor().finalize()

unpadder = PKCS7(algorithms.AES.block_size).unpadder()
print(unpadder.update(padded_res) + unpadder.finalize())
