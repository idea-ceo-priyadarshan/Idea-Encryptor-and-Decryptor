import os

def encrypt_text(text):
    encrypted_text = ''
    for char in text:
        char_ascii = ord(char)
        char_hash = hex(char_ascii)[2:]
        encrypted_text += char_hash.zfill(3) + ' '
    return encrypted_text.strip()

def decrypt_text(short_hash):
    original_text = ''
    hash_values = short_hash.split()
    for hash_value in hash_values:
        char_ascii = int(hash_value, 16)
        original_char = chr(char_ascii)
        original_text += original_char
    return original_text

def read_text_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        return None

def main():
    print("")
    print("--------------------------")
    print("TEXT ENCRYPTOR & DECRYPTOR")
    print("--------------------------")
    print("")
    while True:
        print("")
        print("Do you want to encrypt or decrypt?")
        print("")
        choice = input("Enter your choice: ").lower()
        print("")

        if choice.lower() == "encrypt":
            opinion=input("Before encrypting, make sure you have copied your previous hast.enc file to another location as it will get overwritten. Do you wish to continue (y/n): ")
            print("")
            if opinion.lower()=='y':
                print("Do you want to paste the text or read from a file?")
                print("")
                input_choice = input("Enter 'paste' or 'file': ").lower()
                print("")

                if input_choice == "paste":
                    text = input("Enter the text you want to encrypt: ")
                    print("")
                    encrypted_text = encrypt_text(text)
                    print("The encrypted hash value is:", encrypted_text)
                elif input_choice == "file":
                    filename = input("Enter the name of the text file (with extension .txt): ")
                    print("")
                    if not filename.endswith('.txt'):
                        print("The file must be a text file (.txt)")
                        return
                    text = read_text_file(filename)
                    if text is None:
                        print("File not found. Please make sure the file is in the same directory as this program.")
                        print("")
                        return
                    encrypted_text = encrypt_text(text)
                    print("")
                    print("The encrypted hash value is stored in the same directory as of this program as hash.enc (NOTE: Don't delete it as it will be required for decrypting.) for the reference, here is the encrypted text: \n", encrypted_text)
                    print("")
                    print("The encrypted hash value is stored in the same directory as of this program as hash.enc (NOTE: Don't delete it as it will be required for decrypting.)\n")
                    print("")
                    file = open('hash.enc', 'a+', encoding="utf-8")
                    file.write(encrypted_text)
                    file.close()
                else:
                    print("Invalid input. Please enter 'paste' or 'file'.")
                    print("")
            else:
                continue

        elif choice.lower() == "decrypt":
            print("")
            qwerty=input("Please enter 'paste' or 'file': ")
            if qwerty.lower == 'file':
                filename = input("Enter the name of the encrypted file (with extension .enc): ")
                print("")
                if not filename.endswith('.enc'):
                    print("The file must be an encrypted file (.enc)")
                    print("")
                    return
                if not os.path.exists(filename):
                    print("File not found. Please make sure the file is in the same directory as this program.")
                    print("")
                    return
                with open(filename, 'r') as file:
                    short_hash = file.read()
                    original_text = decrypt_text(short_hash)
                    print("The decrypted text is: \n \n", original_text)
                    print("")
                    file1 = open('decrypted-text.txt', 'a+', encoding="utf-8")
                    file1.write(original_text)
                    print("")
                    print("The output is stored in the same directory as of this Program as 'decrypted-text.txt'.")
                    print("")
                    file1.close()
            elif qwerty.lower=='paste':
                print("")
                oz=input('Enter your encrypted text: ')
                original_text = decrypt_text(oz)
                print("The decrypted text is: \n \n", original_text)
                print("")
                file1 = open('decrypted-text.txt', 'a+', encoding="utf-8")
                file1.write(original_text)
                print("")
                print("The output is stored in the same directory as of this Program as 'decrypted-text.txt'.")
                print("")
                file1.close()
            else:
                print("Invalid input. Please enter 'paste' or 'file'.")
                print("")
        else:
            print("Invalid input. Please enter 'encrypt' or 'decrypt'.")
            print("")
abcd = input("Before continuing, please read the terms and conditions. Do you agree? [y/n]: ")
print("")
if abcd.lower()=='y':
    print("")
    print("------------------")
    print("TERMS & CONDITIONS")
    print("------------------")
    print("")
    print('''1. This program should not be copied, or the code should not be implemented into another program, if so, happens the company has the full right over that product.

2. The program is made for commercial purpose only and is completely FREE and should not be sold at any price at any cost, if so, happens the company has the complete right over the company and can take legal actions based on that.

3. This program is under development and is consider to be in its alpha stage. This program should not be made available to consumers till it is announced on its official website:
ideablogs.000webhostapp.com
It is currently only available for the app testers whom we call as ‘IdeaFilghters’. Anyone can join the waitlist for being a IdeaFilghter by submitting a for which is available on its official website.

4. The company is not responsible for any:
	• Misuse
	• Damage to the user’s PC or Files.
	• Illegal activities made using this program.

5. The program will not show up in the Control Panel cause this is not an actual program, this is a Python file which has been made by Priyadarshan Mahankuda. For steps for uninstallation please read our documentation available on our official website.

6. The program is also currently in development for converting it from Python to an Executable format. Till then you can install Python and use this Program.
''')
    print("")
    abcdef=input("Do you agree? [y/n]: ")
    if abcdef.lower()=='y':
        if __name__ == '__main__':
            main()
    else:
        exit
else:
    exit
