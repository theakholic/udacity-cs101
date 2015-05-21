#-------------------------------------------------------------------------------
# Name:        recursion.py
# Purpose:
#
# Author:      Akshay
#
# Created:     18-05-2015
# Copyright:   (c) Akshay 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def is_palin(s):
    if s == '':
        return True
    if s[0] == s[-1]:
        return is_palin(s[1:-1])
    return False

def list_binary_search_depth(p,e,level = 0):
    if p == []:
        return [False, level]
    mid = len(p)//2
    if len(p) == 1:
        return [p[0] == e,level]
    if p[mid] > e:
        return list_binary_search_depth(p[:mid],e,level+1)
    else:
        return list_binary_search_depth(p[mid:],e,level+1)

def list_binary_search_depth_2(p, e, level = 0):
    if p == []:
        return [False, level]
    if len(p) == 1:
        return [p[0] == e, level]
    mid = len(p)//2
    if p[mid] == e:
        return [True, level]
    if p[mid] < e:
        return list_binary_search_depth_2(p[mid+1:],e,level+1)
    else:
        return list_binary_search_depth_2(p[:mid],e,level+1)


def list_binary_search_where(p,e,start = 0):
    if p == []:
        return [False,None]

    if len(p) == 1:
        if e == p[0]:
            return [True,start]
        else:
            return [False,None]
    mid = len(p)//2
    if p[mid] == e:
        return [True,start + mid]
    if p[mid] < e:
        return list_binary_search_where(p[mid+1:],e,start + mid + 1)
    else:
        return list_binary_search_where(p[:mid],e,start)



def quick_sort(p):
    if p == []:
        return []
    import random
    splitter = p.pop(random.randint(0,len(p) - 1))
    lesser = [x for x in p if x <= splitter]
    greater = [x for x in p if x > splitter]
    return quick_sort(lesser)+ [splitter] +quick_sort(greater)

def popularity(t,p):
    if t == 0:
        return 1
    score = 0
    for f in friends(p):
        score += popularity(t-1,p)
    return score

def make_bricks(small, big, goal):
    if big == 0:
        return small >= goal
    remaining = min((goal//5),big)
    if small >= goal - 5*remaining:
        return True
    return False

def make_chocolate(small, big, goal):
    if big == 0:
        if small < goal:
            return -1
    remaining = min(goal//5, big)
    s = goal - remaining*5
    if s <= small:
        return s
    return -1


def test_list_binary_search_where():
    B = [0, 1, 2, 3, 4, 5, 6, 7,  8,  9, 10, 11, 12, 13, 14, 15]
    A = [1, 2, 3, 3, 3, 6, 8, 9, 13, 13, 14, 17, 21, 22, 23, 25]
    assert( list_binary_search_where( A, 0) == [False, None] )
    print list_binary_search_where( A, 1)
    assert( list_binary_search_where( A, 1) == [True, 0] )
    assert( list_binary_search_where( A, 2) == [True, 1] )
    print list_binary_search_where( A, 13)
    assert( list_binary_search_where( A, 13) == [True, 9] or list_binary_search_where( A, 13) == [True, 8])
    assert( list_binary_search_where( A, 24) == [False, None] )
    print list_binary_search_where(A,25)
    assert( list_binary_search_where( A, 25) == [True, 15] )
    assert( list_binary_search_where( A, 26) == [False, None] )
    print("tests of list_binary_search_where() passed")

def test_list_binary_search_depth():
    A = [1, 2, 3, 3, 3, 6, 8, 9, 13, 13, 14, 17, 21, 22, 23, 25]
    print list_binary_search_depth( A, 0)
    assert( list_binary_search_depth( A, 0) == [False, 4] )
    assert( list_binary_search_depth( A, 1) == [True, 4] )
    assert( list_binary_search_depth( A, 2) == [True, 4] )
    assert( list_binary_search_depth( A, 13) == [True, 4] )
    assert( list_binary_search_depth( A, 24) == [False, 4] )
    assert( list_binary_search_depth( A, 25) == [True, 4] )
    assert( list_binary_search_depth( A, 26) == [False, 4] )
    print("tests of list_binary_search_depth() passed")

def test_is_palin():
    assert(is_palin('malayalam') == True)
    assert(is_palin('a') == True)
    assert(is_palin('ab') == False)
    print("tests of is_palin passed")

def test_list_binary_search_depth_2():
    A = [1, 2, 3, 3, 3, 6, 8, 9, 13, 13, 14, 17, 21, 22, 23, 25]
    print(list_binary_search_depth_2(A, 0))
    assert( list_binary_search_depth_2( A, 0) == [False, 4] )
    assert( list_binary_search_depth_2( A, 1) == [True, 4] )
    assert( list_binary_search_depth_2( A, 2) == [True, 3] )
    assert( list_binary_search_depth_2( A, 13) == [True, 0] )
    assert( list_binary_search_depth_2( A, 24) == [False, 3] )
    assert( list_binary_search_depth_2( A, 25) == [True, 3] )
    assert( list_binary_search_depth_2( A, 26) == [False, 3] )
    print("tests of list_binary_search_depth_2() passed")

def main():
    test_is_palin()
    test_list_binary_search_depth()
    test_list_binary_search_where()
    test_list_binary_search_depth_2()


if __name__ == '__main__':
    main()
