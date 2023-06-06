from cryptography.fernet import Fernet
import shutil

selected_module = "sys-info"
key = b'8Shjz6mNyel8p7qNCETNEqrxBodA2MZbOtsJ6un79EQ='

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        plaintext = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(plaintext)

    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

    print("File encrypted successfully.")



encrypt_file("modules/" + selected_module + "/payload.py", key)
encrypt_file("modules/" + selected_module + "/requirements.txt", key)


shutil.move("modules/" + selected_module + "/payload.py.enc", "payload.py.enc")
shutil.move("modules/" + selected_module + "/requirements.txt.enc", "requirements.txt.enc")


    