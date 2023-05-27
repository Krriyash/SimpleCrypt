import string

# Define letter frequencies in English language
letter_frequencies = {
    'e': 12.70, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97, 'n': 6.75, 's': 6.33, 'h': 6.09,
    'r': 5.99, 'd': 4.25, 'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36, 'f': 2.23,
    'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.29, 'v': 0.98, 'k': 0.77, 'j': 0.15, 'x': 0.15,
    'q': 0.10, 'z': 0.07
}


def calculate_score(decrypted_data):
    score = 0
    for char in decrypted_data.lower():
        if char in string.ascii_lowercase:
            score += letter_frequencies.get(char, 0)
    return score


def decrypt_brute_force(encrypted_data):
    best_score = 0
    best_decryption = ""

    for shift in range(121):
        decrypted_data = ""
        for char in encrypted_data:
            if char.isalpha():
                if char.isupper():
                    decrypted_data += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                else:
                    decrypted_data += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_data += char

        score = calculate_score(decrypted_data)
        if score > best_score:
            best_score = score
            best_decryption = decrypted_data

    print("Best Decryption:", best_decryption)


def main():
    encrypted_data = input("Enter the encrypted data: ")
    decrypt_brute_force(encrypted_data)


if __name__ == "__main__":
    main()
