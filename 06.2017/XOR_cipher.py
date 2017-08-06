from os import urandom

def XOR_cipher(string, key):
    if isinstance(string, str):
        return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(string, key))
    else:
        return bytes([a ^ b for a, b in zip(string, key)])

msg = 'Crypt!'
key = urandom(len(msg))
crypt = XOR_cipher(msg.encode('utf8'), key)
print(crypt)
msg = XOR_cipher(crypt, key).decode('utf8')
print(msg)
