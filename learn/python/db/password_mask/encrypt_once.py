
from cryptography.fernet import Fernet

from password_utiles import encrypt_password

def generate_key():
    """
    Generates a new Fernet key for encryption.
    """
    with open("secret.key", "wb") as key_file:
        key = Fernet.generate_key()
        key_file.write(key)


if __name__ == "__main__":
    # Generate a new key (only do this once)
    # generate_key()

    # Example usage
    password = "balamurugan"
    encrypted = encrypt_password(password)
    print("Encrypted password:", encrypted.decode())
