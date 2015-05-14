#-------------------------------------------------------------------------------
# Name:        find_last.py
# Purpose:     cs101
#
# Author:      Akshay
#
# Created:     14-05-2015
#-------------------------------------------------------------------------------

def find_last(search, target):
    """
    Returns the last occurance of string 'target' in string 'search'.

    """
    ans = -1
    while True:
        if(search.find(target, ans+1) == -1):
            break
        else:
            ans = search.find(target,ans+1)

    return ans


def test():
    q = [('aaaa','a'), ('aaaaa','aa'), ('aaaaa','b'), ('222222222', ''), ('','3'), ('','')]
    a = [3, 3, -1, 9, -1, 0]

    for i in range(len(q)):
        if(not (find_last(q[i][0], q[i][1]) == a[i])):
            print('Test case ' + str(q[i]) + ' failed')
        else:
            print('Test passed')

if __name__ == '__main__':
    test()
