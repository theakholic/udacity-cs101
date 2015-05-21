#-------------------------------------------------------------------------------
# Name:        challenge_practice.py
# Purpose:
#
# Author:      Akshay
#
# Created:     21-05-2015
#-------------------------------------------------------------------------------

def is_path(graph, n1, n2, k):
    """
    Return whether of path of length <= k exists from n1 to n2.
    """
    step = 0
    if k == 0:
        return n2 == n1 and n2 in graph[n1]
    if n2 in graph[n1]:
        return True
    for e in graph[n1]:
        if is_path(graph,e,n2,k-1):
            return True
    return False


small = {}
small['.'] = 0
small['x'] = 1

large = {}
large[0] = '.'
large[1] = 'x'
def get_binary(n):
    s = bin(n)
    s = s[2:]
    while len(s) < 8:
        s = '0'+s
    return s

def get_rule_no(triplet):
    r = ''
    for e in triplet:
        r += str(small[e])
    return int(r,2)

def cellular_automaton(base, rule, n):
    rules = get_binary(rule)
    rules = rules[::-1]

    generation = 0
    previous = base
    while(generation < n):
        next_str = ''
        for i,e in enumerate(previous):
            if i == 0:
                triplet = previous[-1]+previous[:2]
            elif i == len(previous) - 1:
                triplet = previous[i-1:]+previous[0]
            else:
                triplet = previous[i-1:i+2]
            rule_no = get_rule_no(triplet)
            char = large[int(rules[rule_no])]
            next_str += char
        if previous == next_str:
            break
        previous = next_str
        generation += 1

    return previous



def compute_ranks(graph, k):
    """
    Compute page ranks for a graph excluding reciprocal links of length up to and including k.
    """
    d = 0.8 # damping factor
    numloops = 10
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    if not is_path(graph, page, node, k):
                            newrank = newrank + d * (ranks[node]/len(graph[node]))

            newranks[page] = newrank
        ranks = newranks
    return ranks
def test_compute_ranks():
    # For example

    g = {'a': ['a', 'b', 'c'], 'b':['a'], 'c':['d'], 'd':['a']}

    print compute_ranks(g, 0) # the a->a link is reciprocal
    #>>> {'a': 0.26676872354238684, 'c': 0.1216391112164609,
    #     'b': 0.1216391112164609, 'd': 0.1476647842238683}

    print compute_ranks(g, 1) # a->a, a->b, b->a links are reciprocal
    #>>> {'a': 0.14761759762962962, 'c': 0.08936469270123457,
    #     'b': 0.04999999999999999, 'd': 0.12202199703703702}

    print compute_ranks(g, 2)
    # a->a, a->b, b->a, a->c, c->d, d->a links are reciprocal
    # (so all pages end up with the same rank)
    #>>> {'a': 0.04999999999999999, 'c': 0.04999999999999999,
    #     'b': 0.04999999999999999, 'd': 0.04999999999999999}

def test_cellular_automaton():
    print '1'
    print cellular_automaton('.x.x.x.x.', 17, 2)
    #>>> xxxxxxx..
    print '2'
    print cellular_automaton('.x.x.x.x.', 249, 3)
    #>>> .x..x.x.x
    print cellular_automaton('...x....', 125, 1)
    #>>> xx.xxxxx
    print cellular_automaton('...x....', 125, 2)
    #>>> .xxx....
    print cellular_automaton('...x....', 125, 3)
    #>>> .x.xxxxx
    print cellular_automaton('...x....', 125, 4)
    #>>> xxxx...x
    print cellular_automaton('...x....', 125, 5)
    #>>> ...xxx.x
    print cellular_automaton('...x....', 125, 6)
    #>>> xx.x.xxx
    print cellular_automaton('...x....', 125, 7)
    #>>> .xxxxx..
    print cellular_automaton('...x....', 125, 8)
    #>>> .x...xxx
    print cellular_automaton('...x....', 125, 9)
    #>>> xxxx.x.x
    print cellular_automaton('...x....', 125, 10)
    #>>> ...xxxxx

def test_stirling_and_bell():
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

    print bell(1)
    #>>> 1
    print bell(2)
    #>>> 2
    print bell(3)
    #>>> 5
    print bell(4)
    #>>> 15
    print bell(5)
    #>>> 52
    print bell(15)
    #>>> 1382958545

def main():
    test_cellular_automaton()

if __name__ == '__main__':
    main()
