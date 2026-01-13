# ==========================================
# Encryption & Decryption Program
# Uses Double Caesar Cipher
# ==========================================

import os

# Get current folder path (same folder as this script)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

RAW_FILE = os.path.join(BASE_DIR, "raw_text.txt")
ENCRYPTED_FILE = os.path.join(BASE_DIR, "encrypted_text.txt")
DECRYPTED_FILE = os.path.join(BASE_DIR, "decrypted_text.txt")


def encrypt_text(text, shift1, shift2):
    encrypted = ""
    for ch in text:
        if ch.isprintable():
            encrypted += chr((ord(ch) + shift1 + shift2) % 256)
        else:
            encrypted += ch
    return encrypted


def decrypt_text(text, shift1, shift2):
    decrypted = ""
    for ch in text:
        if ch.isprintable():
            decrypted += chr((ord(ch) - shift1 - shift2) % 256)
        else:
            decrypted += ch
    return decrypted


def read_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def write_file(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def main():
    print("=== Encryption & Decryption Program ===")

    shift1 = int(input("Enter shift1 value: "))
    shift2 = int(input("Enter shift2 value: "))

    # Read raw text
    raw_text = read_file(RAW_FILE)

    # Encrypt
    encrypted_text = encrypt_text(raw_text, shift1, shift2)
    write_file(ENCRYPTED_FILE, encrypted_text)

    # Decrypt
    decrypted_text = decrypt_text(encrypted_text, shift1, shift2)
    write_file(DECRYPTED_FILE, decrypted_text)

    # Verification
    if raw_text == decrypted_text:
        print(" Decryption successful: Files match.")
    else:
        print("Decryption failed: Files do not match.")


if __name__ == "__main__":
    main()
