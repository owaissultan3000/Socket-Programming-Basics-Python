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


def decrypt_string(key, hash_string_client, encrypt_string):

    decrypted_string_server = cipher_decrypt(encrypt_string, key)


    hash_string_server = hashlib.sha256(
        decrypted_string_server.encode()).hexdigest()

    if hash_string_server == hash_string_client:
        print("Data Receive Without Manuplation")
    else:
        print("Data Receive With Manuplation")


serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(('0.0.0.0', 8080))
serv.listen(5)

while True:
    conn, addr = serv.accept()
    key = ''
    hash_data = ''
    encryp_data = ''

    while True:
        data = conn.recv(4096)
        if not data: break
        key += data

        conn.send(" ")

    conn.close()
    socket_data = key.split("?")
    print("Data Received From Client",socket_data[0], socket_data[1], socket_data[2])
    decrypt_string(int(socket_data[0]), socket_data[1], socket_data[2])
    
    print ('client disconnected')
    exit()