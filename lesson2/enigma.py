#-------------------------------------------------------------------------------
# Name:        enigma.py
# Purpose:     simulate 3 rotor enigma
#
#
# Author:      Akshay
#
# Created:     14-05-2015
#-------------------------------------------------------------------------------

def interleave(l1, l2):
    """
    Interleaves the two lists.
    Eg l1 = [1,2,3]
       l2 = [6,7]
       interleave(l1,l2) = [1,6,2,7,3]
    """
    len1 = len(l1)
    len2 = len(l2)
    len0 = min(len1,len2)
    result = []
    for i in range(len0):
        result.append(l1[i])
        result.append(l2[i])

    l = l1 if len1 > len2 else l2
    if(l is l2):
        if(len2 == len0):
            return result
    result = result + l[len0:]
    return result



wheel_a = [i for i in range(256)]
wheel_b = wheel_a[::-1]
wheel_c = interleave([2*i + 1 for i in range(128)],[2*i for i in range(128)])

def rotate_A(pos):
    pos = pos+5
    if(pos > 255):
        pos = pos%256
    return pos


def rotate_B(pos):
    pos = pos-7
    if(pos < 0):
        pos = pos + 256
    return pos

def rotate_C(pos):
    pos = pos+33
    if(pos > 255):
        pos = pos%256
    return pos

def txt_to_hexStr(messageTxt):
    hexStr = ''
    for i in messageTxt:
        hexStr += '%02x' % ord(i)
    return hexStr

def hexStr_to_txt(hexStr):
    plaintext = ''
    for i in range(0,len(hexStr),2):
        plaintext += chr(int(hexStr[i:i+2],16))
    return plaintext

def enigma(text, init):
    """
    Takes hexadecimal representation string of text in variable text,
    and a length 3 list init [initA, initB, initC] containing start positions
    of each wheel.
    returns encoded string in hexadecimal representation.
    """
    l = len(text)
    l = l//2
    result = ''
    pos_a = init[0]
    pos_b = init[1]
    pos_c = init[2]
    for i in range(l):
        current_hex = text[2*i:2*i+2]
        n = int(current_hex,16)
        new_hex = n^wheel_a[pos_a]^wheel_b[pos_b]^wheel_c[pos_c]
        temp = hex(new_hex)
        if(i%2 == 1):
            pos_b = rotate_B(pos_b)
        if(i%3 == 2):
            pos_c = rotate_C(pos_c)
        pos_a = rotate_A(pos_a)
        if(len(temp) == 3):
            temp = '0'+temp[-1]
        else:
            temp = temp[-2:]
        result = result + temp
    return result


def test():
    message_1 = "Udacity courses offers education and fun for free"
    wheels_setup1 = [0,0,0]
    expected_cipher1 = 'ab9f6c4a50403054133b0705e38880ffaca0c5c394b9e4bc4652b294b1b1dad6a4c1d8d7642fc285cf8ce0f8aaf0dac023'

    cipher1 = enigma(txt_to_hexStr(message_1),wheels_setup1)
    print "test case 1 encoding message1 (): ", cipher1 == expected_cipher1

    message = hexStr_to_txt(enigma(cipher1,wheels_setup1))
    print "test case 2 decoding cipher1 (): ", message == message_1

    message_2 = "Udacity offers courses from beginner to advanced level"
    wheels_setup2 = [5,10,40]
    expected_cipher2 = 'ab9f6c4a504030541f321412e29ed3bcacb3d1d583b9e4bf5048bcd5a7bdd2d1eaced3c1643dd8cb8e8ef9ebe4f5cdc1662f2017e4e0'

    cipher2 = enigma(txt_to_hexStr(message_2),wheels_setup1)
    print "test case 3 encoding message2 (): ", cipher2 == expected_cipher2

    message = hexStr_to_txt(enigma(cipher2,wheels_setup1))
    print "test case 4 decoding cipher2 (): ", message == message_2

    message_3   = "The Enigma-Code broken, during the World War II, was one of the first massive computing problems"
    wheels_setup3 = [-5,10,40]
    expected_cipher3 = '73b4b59e0131111834d292e3eaeaaf8cc8c3e1eaee3f09026f756eebeeec9ccfe5327b0306001a74b6cad3df8f0c284a6f2309752c98aea2f1542158293e27045420141a2789c0cba0abbd9c8dc3676c684f5658281429480e07e5979bb8a4bd'

    cipher3 = enigma(txt_to_hexStr(message_3),wheels_setup3)
    print "test case 5 encoding message3 (): ", cipher3 == expected_cipher3

    message = hexStr_to_txt(enigma(cipher3,wheels_setup3))
    print "test case 6 decoding cipher3 (): ", message == message_3

if __name__ == '__main__':
    test()
