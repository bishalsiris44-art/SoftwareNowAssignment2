def verify(original, decrypted):
    if original == decrypted:
        print("Decryption successful: Files match.")
    else:
        print("Decryption failed: Files do not match.")
