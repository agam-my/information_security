#source to learn from https://www.anbidev.com/
from Crypto.PublicKey import RSA

secret_code = input('Please input secret :')
key = RSA.generate(1024)
public_key = key.publickey().export_key()
print (public_key)
