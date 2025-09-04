from text_cipher import encrypt_text, decrypt_text
from file_utils import verify_files

def main():
    try:
        shift1 = int(input("Enter shift1: ").strip())
        shift2 = int(input("Enter shift2: ").strip())
    except ValueError:
        print("Please enter integer values for shifts.")
        return

    # Read raw text
    with open("raw_text.txt", "r", encoding="utf-8") as f:
        raw = f.read()

    # Encrypt
    encrypted = encrypt_text(raw, shift1, shift2)
    with open("encrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(encrypted)
    print("Encrypted -> encrypted_text.txt")

    # Decrypt
    decrypted = decrypt_text(encrypted, shift1, shift2)
    with open("decrypted_text.txt", "w", encoding="utf-8") as f:
        f.write(decrypted)
    print("Decrypted -> decrypted_text.txt")

    # Verify
    if verify_files("raw_text.txt", "decrypted_text.txt"):
        print("Decryption successful. Files match.")
    else:
        print("Decryption failed. Files do not match.")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
