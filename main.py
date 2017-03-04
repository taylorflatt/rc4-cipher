import sys
<<<<<<< HEAD
=======
import base64

user_input_plaintext = input("Please enter your message: ")
user_input_key = input("Please enter the key: ")

plaintext = base64.b64decode(user_input_plaintext)
>>>>>>> c1ae31ad6abe2e9c44cc26634d8bc64f363c5a82

def ksa(key):
    """Produces the key for RC4"""
    j = 0
    s = range(256)

    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) % 256
        s[i], s[j] = s[j], s[i]
    return s
<<<<<<< HEAD

def prga(s):
    i = j = 0
    while True:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        yield s[(s[i] + s[j]) % 256]

def main():
    user_input_plaintext = input("Please enter your message: ").split(' ')
    user_input_plaintext2 = input("Please enter your message: ")
    user_input_key = input("Please enter the key: ").split(' ')

    plaintext = [int(num) for num in user_input_plaintext]
    key = [int(num) for num in user_input_key]
    
    print(plaintext)
    print(key)

if __name__ == "__main__":
    main()
=======
>>>>>>> c1ae31ad6abe2e9c44cc26634d8bc64f363c5a82
