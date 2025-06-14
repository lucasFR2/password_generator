"""
        _            
       / \      _-'  
     _/|  \-''- _ /  
__-' { |          \  
    /             \  
    /       "o.  |o }
    |            \ ; 
                  ', 
       \_         __\
         ''-_    \.//
           / '-____' 
          /          
        _'           
      _-'                      
"""

import json
import os
import secrets
from cryptography.fernet import Fernet
import sys

def options():
    print("""
'##::::'##::::'###:::::'######:::'##::: ##:'####:
 ###::'###:::'## ##:::'##... ##:: ###:: ##:. ##::
 ####'####::'##:. ##:: ##:::..::: ####: ##:: ##::
 ## ### ##:'##:::. ##: ##::'####: ## ## ##:: ##::
 ##. #: ##: #########: ##::: ##:: ##. ####:: ##::
 ##:.:: ##: ##.... ##: ##::: ##:: ##:. ###:: ##::
 ##:::: ##: ##:::: ##:. ######::: ##::. ##:'####:
..:::::..::..:::::..:::......::::..::::..::....::
""")
    print("""
                PASSWORD GENERATOR
          [0] - Exit
          [1] - Generate new password
          [2] - Check if password exists
          [3] - Decrypt and show passwords
          """)            

def return_menu():
    os.system("cls")
    input("\Success. Press Enter to return to the menu.")
    main()

def load_key():
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        print("Failed: Encrypted key not found.")
        sys.exit(1)

def encrypt_data(data, key):
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()

def password_register():
    account_name = input("Which account will this password belong to? \n-> ")
    password_length = int(input("How long will the password be? prefer up to 8 caracters. \n->"))

    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#!$&"
    password = ''.join(secrets.choice(alphabet) for _ in range(password_length))

    print("*SUCCESSFULLY GENERATOR PASSWORD*")

    key = load_key()
    
    encrypted_account = encrypt_data(account_name, key)
    encrypted_password = encrypt_data(password, key)

    data = {
        "EncryptedAccount": encrypted_account, 
        "EncryptedPassword": encrypted_password
    }

    existing_data = []
    if os.path.exists("passwords.json"):
        try:
            with open("passwords.json", "r", encoding="utf-8") as file:
                existing_data = json.load(file)
                if not isinstance(existing_data, list):
                    existing_data = []
        except (json.JSONDecodeError, FileNotFoundError):
            existing_data = []

    existing_data.append(data)


    with open("passwords.json", "w", encoding="utf-8") as file:
        json.dump(existing_data, file, indent=4, ensure_ascii=False)

    print("Data successfully encrypted and saved to 'passwords.json' file.")
    

def password_exists():
    password_input = input("Type the password \n")

    if not os.path.exists("passwords.json"):
        print("No records found. Please register a password first.")
        return_menu()

    try:
        with open("passwords.json", "r", encoding="utf-8") as file:
            data = json.load(file)

            if not isinstance(data, list):
                print("Invalid format in JSON.")
                return_menu()

            key = load_key()
            for registro in data:
                decrypted_password = decrypt_data(registro["EncryptedPassword"], key)
                if decrypted_password == password_input:
                    decrypted_account = decrypt_data(registro["EncryptedAccount"], key)
                    print(f"Password already registered {decrypted_account}")
                    return_menu()

            print("Password not found in the records.")
            return_menu()
    except Exception as e:
        print(f"Password verification failed, {e}")
        return_menu()

def decrypt_data(encrypted, key):
    f = Fernet(key)
    return f.decrypt(encrypted.encode()).decode()

def show_passwords():
    os.system("cls")
    print("""
 ______  _______ _______  ______ __   __  _____  _______
 |     \ |______ |       |_____/   \_/   |_____]    |   
 |_____/ |______ |_____  |    \_    |    |          |   
                                                                                                                                                                                                   
""")
    print("Paste secret key\n")
    
    secret_key = input("Secret key: ").strip() 
    
    try:
        f = Fernet(secret_key.encode())
    except Exception as e:
        print(f"❌ Error: Invalid key.")
        return
    try:
        with open("passwords.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("❌ File 'passwords.json' not found.")
        return
    except json.JSONDecodeError:
        print("❌ Invalid or empty JSON file.")
        return

    os.system("cls")
    print("""
  _____  _______ _______ _______ _  _  _  _____   ______ ______  _______
 |_____] |_____| |______ |______ |  |  | |     | |_____/ |     \ |______
 |       |     | ______| ______| |__|__| |_____| |    \_ |_____/ ______|
                                                                        
""")
    for item in data:
        try:
            account = f.decrypt(item["EncryptedAccount"].encode()).decode()
            decrypted = f.decrypt(item["EncryptedPassword"].encode()).decode()
            print(f"Account: {account}")
            print(f"Password: {decrypted}")
            print("-" * 30)
        except Exception as e:
            print(f"❌ Failed to decrypt account: '{item['Conta']}': {e}")


def choose_option():
    try:
        opt = int(input("Choose one: \n"))
        if opt == 1:
            password_register()
        elif opt == 2:
            password_exists()
        elif opt == 3:
            show_passwords()
        elif opt == 0:
            sys.exit()
        else:
            print("Invalid Option. Please try again.")
            return_menu()
    except ValueError:
        print("Please enter a valid number.")
        return_menu()

def main():
    os.system("cls")
    options()
    choose_option()

if __name__ == '__main__':
    main()