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

# Brianna Yanqui
def decode(encode_pwd):
    decoded = []
    for i in encode_pwd:
        i = int(i) - 3
        decoded.append(i)
    de_coded_s = [str(num) for num in decoded]
    de_coder_str = ''.join(de_coded_s)

    return de_coder_str

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
            # Brianna Yanqui
            de_code = decode(encode_pwd)
            print("The encoded password is", encode_pwd, "and the original password is", de_code, ".")
        elif choose == 3:
            break


main()
