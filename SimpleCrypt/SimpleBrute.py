import io
from collections import Counter


def load_dictionary(file_path):
    with io.open(file_path, 'r', encoding='latin-1') as file:
        dictionary = {word.strip().lower() for word in file}
    return dictionary


def get_letter_frequencies(data):
    total_letters = sum(1 for char in data if char.isalpha())
    letter_counts = Counter(char.lower() for char in data if char.isalpha())
    letter_frequencies = {char: count / total_letters for char, count in letter_counts.items()}
    return letter_frequencies


def decrypt(data, dictionary):
    letter_frequencies = get_letter_frequencies(data)
    decrypted_results = []
    for shift in range(1, 121):
        decrypted_data = ''
        for char in data:
            if char.isalpha():
                if char.islower():
                    decrypted_char = chr((ord(char) - shift - 97) % 26 + 97)
                else:
                    decrypted_char = chr((ord(char) - shift - 65) % 26 + 65)
                decrypted_data += decrypted_char
            else:
                decrypted_data += char

        words = decrypted_data.lower().split()
        word_count = sum(1 for word in words if word in dictionary)
        word_frequency = word_count / len(words) if len(words) > 0 else 0
        letter_frequency = sum(letter_frequencies.get(char.lower(), 0) for char in decrypted_data)
        score = word_frequency * 0.8 + letter_frequency * 0.2
        decrypted_results.append((decrypted_data, shift, score))

    decrypted_results.sort(key=lambda x: x[2], reverse=True)
    return decrypted_results


def main():
    file_path = 'Resources/engmix.txt'  # Replace with the relative file path on your system
    dictionary = load_dictionary(file_path)

    encrypted_data = input("Enter the encrypted data: ")
    results = decrypt(encrypted_data, dictionary)

    print("\nTop 10 Decryption Results:")
    for decrypted_data, shift, score in results[:10]:
        print(f"Shift: {shift:3} | Decrypted Data: {decrypted_data} | Score: {score:.4f}")

    show_all = input("Show all decrypted results? (y/n): ")
    if show_all.lower() == 'y':
        print("\nAll Decryption Results:")
        for decrypted_data, shift, score in results:
            print(f"Shift: {shift:3} | Decrypted Data: {decrypted_data} | Score: {score:.4f}")


if __name__ == "__main__":
    main()
