from encryption import encrypt_text
from decryption import decrypt_text
from verification import verify

def main():
    shift1 = int(input("Enter shift1 value: "))
    shift2 = int(input("Enter shift2 value: "))

    with open("raw_text.txt", "r", encoding="utf-8") as f:
        raw = f.read()

    encrypted = encrypt_text(raw, shift1, shift2)
    with open("encrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(encrypted)

    decrypted = decrypt_text(encrypted, shift1, shift2)
    with open("decrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(decrypted)

    verify(raw, decrypted)

if __name__ == "__main__":
    main()
