#-------------------------------------------------------------------------------
# Name:        median.py
# Purpose:     Find the median of 3 numbers
#
# Author:      Akshay
#
# Created:     14-05-2015
#-------------------------------------------------------------------------------

def bigger(a,b):
    """
    Equivalent to max(a,b).
    Assumes '>' is defined for a and b.
    """
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    """
    Equivalent to max(a,b,c)
    Assumes '>' is defined for a,b,c.
    """
    return bigger(a,bigger(b,c))

def median(a, b, c):
    """
    Returns the median of a,b,c.
    i.e if a >= b >= c, returns b.
    """
    f = bigger(a,b)
    g = biggest(a,b,c)
    if(f == g):
        x = bigger(a,c)
        y = bigger(b,c)
        if( x > y):
            return y
        else:
            return x
    else:
        return f


def test():
    q = [(1,2,3), (9,3,6), (7,8,7)]
    a = [2, 6, 7]

    for i in range(len(q)):
        if(not (median(q[i][0], q[i][1], q[i][2]) == a[i])):
            print('Test case ' + str(q[i]) + ' failed')
        else:
            print('Test passed')

if __name__ == '__main__':
    main()
