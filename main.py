"""RC4 Cipher"""

def ksa(key):
    """Produces the key for RC4"""
    j = 0
    s = list(range(256))

    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) % 256
        s[i], s[j] = s[j], s[i]
    return s

def prga(s):
    """Generator determining random byte stream using key 's'."""
    i = j = 0
    while True:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        yield s[(s[i] + s[j]) % 256]

def rc4(key, plaintext):
    """Encrypts the 'plaintext' using 'key' via the RC4 algorithm."""
    k = ksa(key)
    random = prga(list(k))
    cipher = []

    # XOR the plaintext with the random byte given by k.
    for char in plaintext:
        byte = ord(char)
        c_byte = byte ^ next(random, list(k))
        print("Cipher Byte: ", c_byte)
        cipher.append(chr(c_byte))

    return ''.join(cipher)

def main():
    """Runs the RC4 algorithm by prompting for information and returning their encrypted text."""
    user_input_plaintext = input("Please enter your message: ").split(' ')
    user_input_key = input("Please enter the key: ").split(' ')

    key = [ord(char) for char in user_input_key]

    print(rc4(key, user_input_plaintext))

if __name__ == "__main__":
    main()
