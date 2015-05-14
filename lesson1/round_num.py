#-------------------------------------------------------------------------------
# Name:        round_num
# Purpose:     cs101
#
# Author:      Akshay
#
# Created:     14-05-2015
#-------------------------------------------------------------------------------

def round(num):
    """
    Round float num to the nearest integer and return the integer.
    Note: Only using tools in unit 1
    """

    s = str(num + 0.5)
    point = s.find('.')
    ans = s[:point]
    return int(ans)



def test():
    q = [34.6, -12.4, 0.5, 55]
    a = [35, -11, 1, 55]

    for i in range(len(q)):
        if(not (round(q[i]) == a[i])):
            print('Test case ' + str(q[i]) + ' failed')
        else:
            print('Test passed')

if __name__ == '__main__':
    test()
