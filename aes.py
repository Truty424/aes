import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7

key = os.urandom(32)
iv = os.urandom(16)
nonce = os.urandom(16)

plaintext = b"a secret message"

cipher_enc = Cipher(algorithms.AES(key), modes.CBC(iv))
padder = PKCS7(algorithms.AES.block_size).padder()
padded = padder.update(plaintext) + padder.finalize()

encryptor = cipher_enc.encryptor()
ct = encryptor.update(padded) + encryptor.finalize()

cipher_dec = Cipher(algorithms.AES(key), modes.CTR(nonce))
decryptor = cipher_dec.decryptor()
padded_res = decryptor.update(ct) + decryptor.finalize()

unpadder = PKCS7(algorithms.AES.block_size).unpadder()
unpadded = unpadder.update(padded_res) + unpadder.finalize()

print(unpadded)
