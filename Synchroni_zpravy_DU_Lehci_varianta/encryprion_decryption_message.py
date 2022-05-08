from cryptography import Fernet
from rsa import encrypt

#Třída na zašifrování souboru
#

class Encryptor():

    def key_create(self):
        key = Fernet.generate_key()
        return key
    
    def key_write(self, key, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(key)
        
    def key_load(self, key_name, key):
        with open(key_name, 'rb') as mykey:
            mykey.read()
        return key

#
#   Šifrování souboru pomocí synchroního šifrování
#  


    def file_encrypt(self, key, original_file, encrypted_file):

        f = Fernet(key)

        with open('test.txt', 'rb') as original_file:
            original = original_file.read()


        encrypted = f.encrypt(original)

        with open (encrypted_file, 'wb') as original_file:
            original_file.write(encrypted)
        
#Dešifrování souboru
# 

    def file_decrypt(self, key, original_file, decrypted_file):

        f= Fernet(key)

        with open('test.txt', 'rb') as original_file:
            encrypted = original_file.read()

        decrypted = f.decrypt(encrypted)    