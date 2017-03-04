import sys
import base64

user_input_plaintext = input("Please enter your message: ")
user_input_key = input("Please enter the key: ")

plaintext = base64.b64decode(user_input_plaintext)

def ksa(key):
    """Produces the key for RC4"""
    j = 0
    s = range(256)

    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) % 256
        s[i], s[j] = s[j], s[i]
    return s
