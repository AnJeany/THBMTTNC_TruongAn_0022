import ecdsa, os
from ecies import encrypt as ecies_encrypt, decrypt as ecies_decrypt

class ECCCipher:
    def __init__(self):
        if not os.path.exists('cipher/ecc/keys'):
            os.makedirs('cipher/ecc/keys')

    def generate_keys(self):
        # Bắt buộc dùng SECP256k1 để tương thích với ECIES Encrypt/Decrypt
        sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        vk = sk.get_verifying_key()
        
        with open('cipher/ecc/keys/privateKey.pem', 'wb') as p:
            p.write(sk.to_pem())
        with open('cipher/ecc/keys/publicKey.pem', 'wb') as p:
            p.write(vk.to_pem())

    def load_keys(self):
        with open('cipher/ecc/keys/privateKey.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())
        with open('cipher/ecc/keys/publicKey.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())
        return sk, vk

    def sign(self, message, key):
        return key.sign(message.encode('ascii'))

    def verify(self, message, signature, key):
        try:
            return key.verify(signature, message.encode('ascii'))
        except ecdsa.BadSignatureError:
            return False

    def encrypt(self, message, public_key):
        # Chuyển public key sang định dạng hex của ECIES
        pub_hex = public_key.to_string("compressed").hex()
        encrypted = ecies_encrypt(pub_hex, message.encode('utf-8'))
        return encrypted

    def decrypt(self, ciphertext, private_key):
        # Chuyển private key sang định dạng hex của ECIES
        priv_hex = private_key.to_string().hex()
        decrypted = ecies_decrypt(priv_hex, ciphertext)
        return decrypted.decode('utf-8')