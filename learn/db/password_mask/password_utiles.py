from pathlib import Path

from cryptography.fernet import Fernet


class Fakestr(str):
    def __str__(self):
        return "****"
    def __repr__(self):
        return "****"

def load_key():
    """
    Loads the Fernet key from the secret.key file.
    """
    key_path = Path(__file__).resolve().parents[2] / "secret.key"
    with key_path.open("rb") as key_file:
        key = key_file.read()
    return key

def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password):
    if isinstance(encrypted_password, str):
        encrypted_password = encrypted_password.encode()

    key = load_key()
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return Fakestr(decrypted_password)
    
def get_encrypted_password():
    """
    Reads the encrypted password from a file and returns it.
    """
    encrypted_password = b'gAAAAABqe-gffz9MdxC5EazAoSm_9ZcJZrOyR75UdiRAFKmgcCSu_eVL1m2Y6Yt3zHyCZxL2_cmdmN7CK3cBeV0PmcrNIlOm8Q=='
    
    return decrypt_password(encrypted_password)

if __name__ == "__main__":
    print(get_encrypted_password())
