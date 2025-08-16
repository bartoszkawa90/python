#cezar_crypt
alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

def crypt(choice='decode',shift=0,message=''):
    if type(message) not in  [str]:
        raise TypeError("Message must be string")
    else:
        for i in message:
            if i not in alphabet:
                return message

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

    return message

#print(crypt('encode',1,123))