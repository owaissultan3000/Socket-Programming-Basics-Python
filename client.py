import socket
import uuid
import hashlib
from cryptography.fernet import Fernet


def encrypt_string(message, key):

    salt = uuid.uuid4().hex
    merged = str(salt) + message
    encrypted_string = ""
    fernet = Fernet(key)

    encrypted_string = fernet.encrypt(merged.encode()).decode()

    hash_string = hashlib.sha256(merged.encode()).hexdigest()

    return fernet, hash_string, encrypted_string

message = "my name is owais"
key = Fernet.generate_key()
(fernet, hash_string, encrypt_string) = encrypt_string(message, key)

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8080))
serv.listen(5)
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data
        print("from_client", from_client)
        conn.send(fernet)
        conn.send(hash_string)
        conn.send(encrypt_string)
    conn.close()
    print ('client disconnected')
    exit()