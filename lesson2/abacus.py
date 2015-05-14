#-------------------------------------------------------------------------------
# Name:        abacus.py
# Purpose:    Define a procedure print_abacus(integer) that takes a positive integer
#             and prints a visual representation (image) of an abacus setup for a
#             given positive integer value.
#
#             Ranking
#             1 STAR: solved the problem!
#             2 STARS: 6 < lines <= 9
#             3 STARS: 3 < lines <= 6
#             4 STARS: 0 < lines <= 3
#
# Author:      Akshay
#
# Created:     14-05-2015
# Copyright:   (c) Akshay 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def print_abacus(n):
    """
    prints the abacus representation of n

    """
    #convert the number to 10 digits.
    s = (10 - len(str(n)))*'0'+ str(n)

    #print zeros then asterisks then spaces then remainder zeros then remainder asterisks
    for i in range(10):
        print ('|' + ( (10 - int(s[i])) if (int(s[i]) > 5) else 5)*'0' + ((5 - int(s[i])) if (int(s[i]) <= 5) else 0)*'*' + '   ' + ( (int(s[i]) - 5) if (int(s[i] > 5)) else 0)*'0' + ((int(s[i])) if(int(s[i]) <= 5) else 5)*'*' +'|')


if __name__ == '__main__':
    ###  TEST CASES
    print "Abacus showing 0:"
    print_abacus(0)
    #>>>|00000*****   |
    #>>>|00000*****   |
    #>>>|00000*****   |
    #>>>|00000*****   |
    #>>>|00000*****   |
    #>>>|00000*****   |
    #>>>|00000*****   |
    #>>>|00000*****   |
    #>>>|00000*****   |
    #>>>|00000*****   |
    print "Abacus showing 12345678:"
    print_abacus(12345678)
    #>>>|00000*****   |
    #>>>|00000*****   |
    #>>>|00000****   *|
    #>>>|00000***   **|
    #>>>|00000**   ***|
    #>>>|00000*   ****|
    #>>>|00000   *****|
    #>>>|0000   0*****|
    #>>>|000   00*****|
    #>>>|00   000*****|
    print "Abacus showing 1337:"
    print_abacus(1337)
    #>>>|00000*****   |
    #>>>|00000*****   |
    #>>>|00000*****   |
    #>>>|00000*****   |
    #>>>|00000*****   |
    #>>>|00000*****   |
    #>>>|00000****   *|
    #>>>|00000**   ***|
    #>>>|00000**   ***|
    #>>>|000   00*****|
