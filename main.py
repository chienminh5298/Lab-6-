# Minh C Nguyen

def encode():
    pwd = input("Please enter your password to encode: ")
    result = ''
    for i in pwd:
        i = int(i) + 3
        if i >= 10:
            result += str(i)[-1]  # parse to string then take last digit
        else:
            result += str(i)
    print("Your password has been encoded and stored!")
    return result


def main():
    encode_pwd = ''
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        choose = int(input("Please enter an option: "))

        if choose == 1:
            encode_pwd = encode()
            print(encode_pwd)
        elif choose == 2:
            # decode here
            print("decode here")
        elif choose == 3:
            break


main()
