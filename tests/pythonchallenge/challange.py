def level_0():
    print (2**4)
    print (2**38)


def level_1():
    in_txt = "map"
    out_txt=''

    for c in in_txt:
        out_txt =  out_txt + chr(ord(c)+2)
        # print(chr(c))
    print (in_txt , " -->  " , out_txt)


# Level -2
#--------------
def level_2():
    from urllib.request import urlopen
    import re

    request = urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")

    # a = request.read()
    # b = a.decode("utf-8")
    #
    # d = re.findall('[a-z]', b)
    #
    # e = ''.join(d)
    #
    data = request.readlines()
    encrypted_message = map(lambda bytes: bytes.decode("utf-8"), data[37:1257])
    rare_chars = re.findall('[a-zA-Z]+', ''.join(encrypted_message))
    message = ''.join(rare_chars)

    print(message)


def test():
     x= ['a', 'b', 'c', 'd']
     print ('#'.join(x))
level_2()
#test()