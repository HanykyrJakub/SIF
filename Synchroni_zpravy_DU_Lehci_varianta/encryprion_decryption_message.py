from cryptography.fernet import Fernet

zprava = "Survive..."

key = Fernet.generate_key()

fernet = Fernet(key)

endzpravy = fernet.encrypt(zprava.encode())

print("originální zpráva: ", zprava)
print("Zašifrovaný zpráva: ", endzpravy)

des_zpravy = fernet.decrypt(endzpravy).decode()

print("dešifrovaný zpráva: ", des_zpravy)
