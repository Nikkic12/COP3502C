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
            pass
        elif option_input == 3:
            break
if __name__ == "__main__":
    main()