# verification.py
# Compares original and decrypted text

def verify(original_text, decrypted_text):
    if original_text == decrypted_text:
        print("Decryption successful: Files match.")
    else:
        print("Decryption failed: Files do not match.")
