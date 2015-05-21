#-------------------------------------------------------------------------------
# Name:        recursion_practicee
# Purpose:
#
# Author:      Akshay
#
# Created:     21-05-2015
#-------------------------------------------------------------------------------

def rec_print(p):
    """Print the elements of a list, each on a separate line."""
    if len(p) == 0:
        return
    t = p.pop(0)
    print t
    rec_print(p)

def iter_print(p):
    for e in p:
        print e

def rec_increment(p):
    """Return a list of numbers with each of its elements increased by 1."""
    if p == []:
        return []
    t = p.pop()
    return [t+1] + rec_increment(p)

def iter_increment(p):
    return [x+1 for x in p]

def rec_AbSum(p):
    """Return the sum of the absolute values of the numbers in a list.
    Use the built-in abs (e.g. abs(-5) == 5)."""
    if p == []:
        return 0
    return abs(p.pop()) +  rec_AbSum(p)

def iter_AbSum(p):
    sum = 0
    for e in p:
        sum += abs(e)
    return sum

def rec_median(p):
    """Find the median of a sorted (assume that) list of numbers."""

    if len(p) <= 2:
        return p[-1]


    return rec_median(p[1:-1])


def iter_median(p):
    assert len(p) > 0
    pos = 0
    width = len(p)
    while width > 2:
        pos = pos+1
        width = width - 2
    if width == 2:
        return p[pos+1]
    return p[pos]


def rec_RemDup(p):
    """Remove duplicate entries in a list."""
    if p == []:
        return []

    current = p.pop(0)
    remaining = [t for t in p if t != current]
    return [current]+rec_RemDup(remaining)



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


def cross_product(p,q):
    #[1,2,3]*[4,5] = [(1,4),(1,5),(2,4)
    res = []
    for e in p:
        for f in q:
            res.append((e,f))

    return res

def is_list(p):
    return isinstance(p,list)

def flatten(p):
    result = []
    if p == []:
        return []
    for e in p:
        if is_list(e):
            result+=flatten(e)
        else:
            result.append(e)
    return result


cache = []
for i in range(40):
    cache.append([-1]*40)
    cache[i][1] = 1

for i in range(40):
    for j in range(40):
        if i < j:
            cache[i][j] = 0


def stirling(n,k):
    if cache[n][k] == -1:
        cache[n][k] = k*stirling(n-1,k) + stirling(n-1,k-1)
    return cache[n][k]



print stirling(1,1)
#>>> 1
print stirling(2,1)
#>>> 1
print stirling(2,2)
#>>> 1
print stirling(2,3)
#>>>0

print stirling(3,1)
#>>> 1
print stirling(3,2)
#>>> 3
print stirling(3,3)
#>>> 1
print stirling(4,1)
#>>> 1
print stirling(4,2)
#>>> 7
print stirling(4,3)
#>>> 6
print stirling(4,4)
#>>> 1

print stirling(5,1)
#>>> 1
print stirling(5,2)
#>>> 15
print stirling(5,3)
#>>> 25
print stirling(5,4)
#>>> 10
print stirling(5,5)
#>>> 1

print stirling(20,15)
#>>> 452329200



def main():
    print(rec_median([1,2,3,5,7,8,9,10]))
    print(rec_RemDup([1,23,55,33,23,5,16, 1,1, 5, 33, 55, 16,24]))

if __name__ == '__main__':
    main()
