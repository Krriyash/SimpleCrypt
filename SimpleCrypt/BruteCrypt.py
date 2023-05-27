def decrypt_brute_force(encrypted_data):
    for shift in range(301):
        decrypted_data = ""
        for char in encrypted_data:
            if char.isalpha():
                if char.isupper():
                    decrypted_data += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                else:
                    decrypted_data += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_data += char
        print(f"Striking.. (Shift = {shift}):", decrypted_data)


def main():
    encrypted_data = input("Enter the encrypted data: ")
    decrypt_brute_force(encrypted_data)


if __name__ == "__main__":
    main()
