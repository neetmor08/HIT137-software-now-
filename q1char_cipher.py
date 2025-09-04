def encrypt_char_halfwrap(ch, shift1, shift2):
    if 'a' <= ch <= 'm':
        idx = ord(ch) - ord('a')
        shift = (shift1 * shift2) % 13
        return chr(ord('a') + ((idx + shift) % 13))
    elif 'n' <= ch <= 'z':
        idx = ord(ch) - ord('n')
        shift = (shift1 + shift2) % 13
        return chr(ord('n') + ((idx - shift) % 13))
    elif 'A' <= ch <= 'M':
        idx = ord(ch) - ord('A')
        shift = shift1 % 13
        return chr(ord('A') + ((idx - shift) % 13))
    elif 'N' <= ch <= 'Z':
        idx = ord(ch) - ord('N')
        shift = (shift2 ** 2) % 13
        return chr(ord('N') + ((idx + shift) % 13))
    else:
        return ch

def decrypt_char_halfwrap(ch, shift1, shift2):
    if 'a' <= ch <= 'm':
        idx = ord(ch) - ord('a')
        shift = (shift1 * shift2) % 13
        return chr(ord('a') + ((idx - shift) % 13))
    elif 'n' <= ch <= 'z':
        idx = ord(ch) - ord('n')
        shift = (shift1 + shift2) % 13
        return chr(ord('n') + ((idx + shift) % 13))
    elif 'A' <= ch <= 'M':
        idx = ord(ch) - ord('A')
        shift = shift1 % 13
        return chr(ord('A') + ((idx + shift) % 13))
    elif 'N' <= ch <= 'Z':
        idx = ord(ch) - ord('N')
        shift = (shift2 ** 2) % 13
        return chr(ord('N') + ((idx - shift) % 13))
    else:
        return ch

if __name__ == "__main__":
    print("Character-level encryption/decryption implemented ")
