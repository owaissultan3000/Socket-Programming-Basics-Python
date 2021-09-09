import socket
import hashlib


def decrypt_string(hash_string, fernet, encrypt_string):

    decrypted_string_server = fernet.decrypt(encrypt_string.encode()).decode()


    hash_string_server = hashlib.sha256(
        decrypted_string_server.encode()).hexdigest()

    if hash_string_server == hash_string:
        return True
    else:
        return False


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8080))

fernet = client.recv(4096)
hash_string = client.recv(4096)
encrypt_string = client.recv(4096)

result = decrypt_string(hash_string, fernet, encrypt_string)
if result:
    client.send("Data Receive Without Manuplation")
else:
    client.send("Data Receive With Manuplation")
client.close()
