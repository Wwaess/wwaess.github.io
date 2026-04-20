# This is a text/file encrypter that relies on the XOR
# operator to encrypt and decrypt data.
# The key is a string that is used to perform
# the XOR operation on each byte of the data.
# Base64 is used so encrypted output can be stored safely.

from itertools import cycle
import base64
import os

print("Current working directory:")
print(os.getcwd())

def xor_process(data, key):
    # convert key to bytes and repeat it
    key_bytes = key.encode('utf-8')
    return bytes([b ^ k for b, k in zip(data, cycle(key_bytes))])


def encrypt(text, key="default", encode=False, decode=False):

    # if we're decoding, undo base64 first
    if decode:
        data = base64.b64decode(text.encode('utf-8'))
    else:
        data = text.encode('utf-8')

    # XOR the data
    xored = xor_process(data, key)

    # if encoding, apply base64 so it's safe to store
    if encode:
        return base64.b64encode(xored).decode('utf-8')

    # otherwise just return normal text
    return xored.decode('utf-8')


# -------- FILE FUNCTIONS -------- #

def encrypt_file(input_file, output_file, key):

    # read file as raw bytes
    with open(input_file, "rb") as f:
        data = f.read()

    # XOR then base64 encode
    xored = xor_process(data, key)
    encoded = base64.b64encode(xored)

    # save encrypted file
    with open(output_file, "wb") as f:
        f.write(encoded)

    print("Encrypted file saved as", output_file)


def decrypt_file(input_file, output_file, key):

    # read encrypted file
    with open(input_file, "rb") as f:
        data = f.read()

    # undo base64 then XOR
    decoded = base64.b64decode(data)
    original = xor_process(decoded, key)

    # save decrypted file
    with open(output_file, "wb") as f:
        f.write(original)

    print("Decrypted file saved as", output_file)


# -------- EXAMPLE -------- #

def run_example(key):
    original_text = "XOR procedure"

    encrypted_text = encrypt(original_text, key, encode=True)
    decrypted_text = encrypt(encrypted_text, key, decode=True)

    print("Original:", original_text)
    print("Encrypted:", encrypted_text)
    print("Decrypted:", decrypted_text)


if __name__ == "__main__":
    encryption_key = "thisisabadencryptionkey"
    run_example(encryption_key)

    # file demo (uncomment to use)
    # encrypt_file("input.txt", "encrypted.txt", encryption_key)
    # decrypt_file("encrypted.txt", "decrypted.txt", encryption_key)