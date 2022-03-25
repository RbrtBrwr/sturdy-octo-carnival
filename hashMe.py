from base64 import encode
from hashlib import sha256

def hashMe(string):
    nombre = string
    encoded = sha256(nombre.encode())
    newName = int(encoded.hexdigest(), 16)
    print(newName)
    print(newName % 2)