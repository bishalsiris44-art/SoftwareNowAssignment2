# decryption.py
# Handles decryption logic only

def decrypt_text(text, shift1, shift2):
    decrypted = ""

    for ch in text:
        if ch.islower():
            if 'a' <= ch <= 'm':
                decrypted += chr((ord(ch) - ord('a') - (shift1 * shift2)) % 26 + ord('a'))
            else:
                decrypted += chr((ord(ch) - ord('a') + (shift1 + shift2)) % 26 + ord('a'))

        elif ch.isupper():
            if 'A' <= ch <= 'M':
                decrypted += chr((ord(ch) - ord('A') + shift1) % 26 + ord('A'))
            else:
                decrypted += chr((ord(ch) - ord('A') - (shift2 ** 2)) % 26 + ord('A'))

        else:
            decrypted += ch

    return decrypted
