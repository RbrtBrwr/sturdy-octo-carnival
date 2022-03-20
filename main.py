from base64 import encode
from hashlib import sha256

def hashMe(string):
    nombre = string
    encoded = sha256(nombre.encode())
    newName = int(encoded.hexdigest(), 16)
    print(newName)
    print(newName % 2)


testHashing('Pedro')
testHashing('PEDRO')
testHashing('PedRO')
testHashing('juan')
testHashing('Las aventuras de los ninos que caminan')
testHashing('miguel')
testHashing('a')
testHashing('askhbdlhsdbf')
testHashing('sdoerwjgewrj')
testHashing('sherlock holmes')
testHashing('Coding for Beginners')
testHashing('Hito de Arquitectura')
