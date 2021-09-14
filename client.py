import socket
import uuid
import hashlib


# The Encryption Function
def cipher_encrypt(plain_text, key):

    encrypted = ""

    for c in plain_text:

        if c.isupper():  #check if it's an uppercase character

            c_index = ord(c) - ord('A')

            # shift the current character by key positions
            c_shifted = (c_index + key) % 26 + ord('A')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.islower():  #check if its a lowecase character

            # subtract the unicode of 'a' to get index in [0-25) range
            c_index = ord(c) - ord('a')

            c_shifted = (c_index + key) % 26 + ord('a')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.isdigit():

            # if it's a number,shift its actual value
            c_new = (int(c) + key) % 10

            encrypted += str(c_new)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            encrypted += c

    return encrypted


def encrypt_string(message, key):

    salt = uuid.uuid4().hex
    merged = str(salt) + message
    encrypted_string = ""


    encrypted_string = cipher_encrypt(merged, key)

    hash_string = hashlib.sha256(merged.encode()).hexdigest()

    return hash_string, encrypted_string

message = 'OwaisSultan'
key = 3
print("Message Before Encryption: " + message)
print("Cipher Key Value: ", + key)
(hash_string, encrypt_string) = encrypt_string(message, key)
print ("Encrypted Message: " + encrypt_string)
print("Hash Of Message: " + hash_string)


socket_data = str(key) + "?" + str(hash_string) + "?" + str(encrypt_string)
print(socket_data)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8080))

client.send(socket_data)

from_server = client.recv(4096)

client.close()

