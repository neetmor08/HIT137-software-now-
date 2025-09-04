from char_cipher import encrypt_char_halfwrap, decrypt_char_halfwrap

def encrypt_text(text, s1, s2):
    """Encrypt full string using halfwrap cipher."""
    return "".join(encrypt_char_halfwrap(ch, s1, s2) for ch in text)

def decrypt_text(text, s1, s2):
    """Decrypt full string using halfwrap cipher."""
    return "".join(decrypt_char_halfwrap(ch, s1, s2) for ch in text)

if __name__ == "__main__":
    print("Text-level encryption and decryption functions implemented ")
