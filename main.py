def encoder(password):  # Nikki Chen
    string = ""
    for i in password:
        if i == "9":
            i = -1
            x = int(i) + 3
        elif i == "8":
            i = -2
            x = int(i) + 3
        elif i == "7":
            i = -3
            x = int(i) + 3
        elif i == i:
            x = int(i) + 3
        string += str(x)
    return string

def decode(password):
    decoded_pass = ""
    for i in password:
        if i == "0":
            decoded_pass += "7"
        elif i == "1":
            decoded_pass += "8"
        elif i == "2":
            decoded_pass += "9"
        else:
            decoded_pass += str(int(i) - 3)
    return decoded_pass

def main():
    program_continues = True
    while program_continues:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        option_input = int(input("Please enter an option: "))
        if option_input == 1:
            password_to_encode = input("Please enter your password to encode: ")
            encoded_password = encoder(password_to_encode)
            print("Your password has been encoded and stored!")
        elif option_input == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")
        elif option_input == 3:
            break
if __name__ == "__main__":
    main()