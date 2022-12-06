import codecs
import binascii
import re
import base64


def remove(string):
    pattern = re.compile(r'\s+')
    return re.sub(pattern, '', string)


def octal_to_string(octal_str):
    str_converted = ''
    for octal_Char in octal_str.split():
        str_converted += chr(int(octal_Char, 8))
    return str_converted


while True:
    choice = input(
        "what is the base hexadecimal ,binary, decimal, octal,  base64 choose 1, 2, 3, 4, 5: ")
    if choice == "1":
        fromhex = input('input hex string: ')
        remove(fromhex)
        hex_to_asc11 = codecs.decode(remove(fromhex), 'hex').decode('ASCII')
        print(hex_to_asc11)

    elif choice == '2':
        frombin = input("input binary: ")
        no_space = int(frombin.replace(' ', ''), 2)
        total_bytes = (no_space.bit_length() + 7) // 8
        input_array = no_space.to_bytes(total_bytes, 'big')
        ASCII_value = input_array.decode()
        print(ASCII_value)

    elif choice == '3':
        decimal_string = input("input decimal: ")
        number_li = decimal_string.split()
        for i in range(len(number_li)):
            number_li[i] = int(number_li[i])
        for number in number_li:
            char = chr(number)
            print("Character of ASCII value", number, "is ", char)

    elif choice == '4':
        octal_string = input('input octal: ')
        print(octal_to_string(octal_string))

    elif choice == '5':
        base = input('input base64 here')
        decode = base64.b64decode(base).decode('UTF-8')
        print(decode)
