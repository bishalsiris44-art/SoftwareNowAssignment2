def decrypt_text(text, shift1, shift2):
    result = ""

    for ch in text:
        if 'a' <= ch <= 'm':
            result += chr((ord(ch) - ord('a') - shift1 * shift2) % 13 + ord('a'))

        elif 'n' <= ch <= 'z':
            result += chr((ord(ch) - ord('n') + (shift1 + shift2)) % 13 + ord('n'))

        elif 'A' <= ch <= 'M':
            result += chr((ord(ch) - ord('A') + shift1) % 13 + ord('A'))

        elif 'N' <= ch <= 'Z':
            result += chr((ord(ch) - ord('N') - shift2 ** 2) % 13 + ord('N'))

        else:
            result += ch

    return result
