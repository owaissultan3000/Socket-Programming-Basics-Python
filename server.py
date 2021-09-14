import socket
import hashlib


# The Decryption Function
def cipher_decrypt(ciphertext, key):

    decrypted = ""

    for c in ciphertext:

        if c.isupper():

            c_index = ord(c) - ord('A')

            # shift the current character to left by key positions to get its original position
            c_og_pos = (c_index - key) % 26 + ord('A')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.islower():

            c_index = ord(c) - ord('a')

            c_og_pos = (c_index - key) % 26 + ord('a')

            c_og = chr(c_og_pos)

            decrypted += c_og

        elif c.isdigit():

            # if it's a number,shift its actual value
            c_og = (int(c) - key) % 10

            decrypted += str(c_og)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            decrypted += c

    return decrypted


def decrypt_string(hash_string, key, encrypt_string):

    decrypted_string_server = cipher_decrypt(encrypt_string, key)


    hash_string_server = hashlib.sha256(
        decrypted_string_server.encode()).hexdigest()

    if hash_string_server == hash_string:
        return True
    else:
        return False


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8080))

# key = client.recv(4096)
# hash_string = client.recv(4096)
encrypt_string = client.recv(4096)
print(encrypt_string)

# result = decrypt_string(hash_string, key, encrypt_string)
# if result:
#     client.send("Data Receive Without Manuplation")
# else:
#     client.send("Data Receive With Manuplation")
client.close()
