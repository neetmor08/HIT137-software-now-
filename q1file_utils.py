def verify_files(file1, file2):
    """Compare two files and return True if contents match."""
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        return f1.read() == f2.read()

if __name__ == "__main__":
    print("File verification utility implemented ")
