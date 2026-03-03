import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7

key = os.urandom(32)
iv = os.urandom(16)

cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
padder = PKCS7(algorithms.AES.block_size).padder()
padded = padder.update(b"a secret message") + padder.finalize()

ct = cipher.encryptor().update(padded) + cipher.encryptor().finalize()
padded_res = cipher.decryptor().update(ct) + cipher.decryptor().finalize()

unpadder = PKCS7(algorithms.AES.block_size).unpadder()
print(unpadder.update(padded_res) + unpadder.finalize())
