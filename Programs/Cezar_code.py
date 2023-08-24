
import numpy as np
alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

def crypt(choice='decode',shift=0,message=''):
    if message == '':
        return 'You_did_not_give_any_message'
    else:
        if choice=='decode':
            shift = -1 * shift
        for i in range(len(message)):
            if message[i] in alphabet:
                message = list(message)
                index = int(alphabet.index(message[i]))
                message[i] = alphabet[(index + shift) % len(alphabet)]
                message = ''.join(message)
            else:
                continue
        #print("It is the encoded result : " , message)
    return message

#
# logo = """
#  ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
# a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
# 8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
# "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
#  `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
#             88             88
#            ""             88
#                           88
#  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
# a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
# 8b         88 88       d8 88       88 8PP""""""" 88
# "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
#  `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
#               88
#               88
# """
# print(logo)
#
#
#
#
# k='yes'
#
# while k=='yes':
#     choice = input("Type 'encode' to encrypt , or type 'decode' to decrypt : ")
#     if choice == '':
#         print("You did not enter anything")
#         continue
#     message = input("Type your message ").lower()
#     while True:
#         try:
#             shift = int(input("Type your shift number "))
#             break
#         except ValueError:
#             print("You should write a number not a word")
#             continue
#         else:
#             continue
#
#
#     print("It is the encoded result : ",crypt(choice,shift, message))
#
#     k = input('Type "yes" if you want to go again. Otherwise type "no" ')
