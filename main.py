# main.py
# Controls the program flow

from encryption import encrypt_text
from decryption import decrypt_text
from verification import verify

def main():
    shift1 = int(input("Enter shift1 value: "))
    shift2 = int(input("Enter shift2 value: "))

    # Read raw file
    with open("raw_text.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()

    # Encrypt
    encrypted_text = encrypt_text(raw_text, shift1, shift2)
    with open("encrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(encrypted_text)

    # Decrypt
    decrypted_text = decrypt_text(encrypted_text, shift1, shift2)
    with open("decrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(decrypted_text)

    # Verify
    verify(raw_text, decrypted_text)


if __name__ == "__main__":
    main()
