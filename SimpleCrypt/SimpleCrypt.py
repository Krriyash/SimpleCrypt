def encrypt(data, shift):
    encrypted = ""
    for char in data:
        if char.isalpha():
            if char.isupper():
                encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted += char
    return encrypted


def decrypt(data, shift):
    return encrypt(data, -shift)


def main():
    choice = input("Choose an option (1. Encrypt, 2. Decrypt): ")
    if choice == "1":
        data = input("Enter the data you want to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_data = encrypt(data, shift)
        key = f"Shift: {shift}"
        print("Encrypted data:", encrypted_data)
        print("Encryption key:", key)
        # Save the encrypted_data and key to a file or database
    elif choice == "2":
        key = input("Enter the encryption key (format: Shift: <shift_value>): ")
        encrypted_data = input("Enter the encrypted data: ")
        try:
            shift = int(key.split(": ")[1])
            decrypted_data = decrypt(encrypted_data, shift)
            print("Decrypted data:", decrypted_data)
        except IndexError:
            print("Invalid encryption key format.")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()