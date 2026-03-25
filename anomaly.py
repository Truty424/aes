import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.primitives.asymmetric import rsa, padding, ed25519, x25519
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.keywrap import aes_key_unwrap


def chacha20_mode_none():
    key = os.urandom(32)
    nonce = os.urandom(16)

    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None)
    data = b"secret message"
    out = cipher.encryptor().update(data) + cipher.encryptor().finalize()
    print(out)


def rsa_verify():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    msg = b"hello"
    sig = private_key.sign(msg, padding.PKCS1v15(), hashes.SHA256())

    public_key.verify(sig, msg, padding.PKCS1v15(), hashes.SHA256())
    print("rsa verify ok")


def aes_unwrap():
    wrapping_key = os.urandom(16)
    wrapped_key = bytes.fromhex("1fa68b0a8112b447aeF34bd8fb5a7b82"
                                "9d3e862371d2cfe5")
    unwrapped = aes_key_unwrap(wrapping_key, wrapped_key)
    print(unwrapped)


def ed25519_sign_verify():
    private_key = ed25519.Ed25519PrivateKey.generate()
    public_key = private_key.public_key()

    msg = b"hello"
    sig = private_key.sign(msg)
    public_key.verify(sig, msg)
    print("ed25519 ok")


def x25519_exchange():
    private_key_1 = x25519.X25519PrivateKey.generate()
    private_key_2 = x25519.X25519PrivateKey.generate()

    shared = private_key_1.exchange(private_key_2.public_key())
    print(shared)


if __name__ == "__main__":
    chacha20_mode_none()
    rsa_verify()
    ed25519_sign_verify()
    x25519_exchange()
    # aes_unwrap()  # optional, depends on valid wrapped test vector
