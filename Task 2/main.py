def shift_text(message, step):
    output = ""

    for symbol in message:
        if symbol.isalpha():
            base_code = ord("A") if symbol.isupper() else ord("a")
            moved_char = chr((ord(symbol) - base_code + step) % 26 + base_code)
            output += moved_char
        else:
            output += symbol

    return output


def encrypt_text_file(file_path, step):
    try:
        with open(file_path, "r", encoding="utf-8") as source_file:
            original_text = source_file.read()

        locked_text = shift_text(original_text, step)

        with open("encrypted_" + file_path, "w", encoding="utf-8") as target_file:
            target_file.write(locked_text)

        print("File encrypted successfully!")

    except FileNotFoundError:
        print("File not found.")


def decrypt_text_file(file_path, step):
    try:
        with open(file_path, "r", encoding="utf-8") as source_file:
            encrypted_text = source_file.read()

        restored_text = shift_text(encrypted_text, -step)

        with open("decrypted_" + file_path, "w", encoding="utf-8") as target_file:
            target_file.write(restored_text)

        print("File decrypted successfully!")

    except FileNotFoundError:
        print("File not found.")


def main():
    print("===== File Encryption/Decryption Tool =====")
    print("1. Encrypt File")
    print("2. Decrypt File")

    user_choice = input("Enter choice (1/2): ").strip()
    file_name = input("Enter file name (with extension): ").strip()

    try:
        shift_value = int(input("Enter shift value (e.g., 3): ").strip())
    except ValueError:
        print("Invalid shift value. Please enter a number.")
        return

    if user_choice == "1":
        encrypt_text_file(file_name, shift_value)
    elif user_choice == "2":
        decrypt_text_file(file_name, shift_value)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()