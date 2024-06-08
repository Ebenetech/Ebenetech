from cryptography.fernet import Fernet


'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()'''




def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key 


root_password = input("Enter your master password: ")
key = load_key() + root_password.encode()
fer = Fernet(key)


def view():
    with open("Passkey.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "Password:", fer.decrypt(passw.encode()).decode())
                    
def add():
    name = input("Enter your name: ")
    password = input("Password: ")

    with open("Passkey.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")




while True:
    mode = input("Would you like to add a new password or view existing passwords(view, add) ? q to quit: ")
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Mode.❌")
        continue