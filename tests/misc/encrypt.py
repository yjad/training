alphabet= 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.!?0123456789, '
upper_index = len(alphabet) - 1
key = 3


def encrypt(input_str:str):
    out_str: str = ""
    for c in input_str:
        p = alphabet.find(c)
        p += key
        if p >= upper_index:
            p -= (upper_index +1)
        out_str += alphabet[p]
    return out_str


def decrypt(out_str):
    str = ""
    for c in out_str:
        p = alphabet.find(c)
        p -= key
        if p < 0:
            p += (upper_index +1)
            #print (f'{alphabet.find(c)}, final: {p}')
        str += alphabet[p]
    #print ('from dectupt:', str)
    return str


for x in range(5):
    input_str = input("Enter str to encrypt: ")
    encrypted_str = encrypt(input_str)
    print (encrypted_str)


    print (decrypt(encrypted_str))
