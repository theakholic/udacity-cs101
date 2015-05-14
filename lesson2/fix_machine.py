#-------------------------------------------------------------------------------
# Name:        fix_machine.py
# Purpose:      Write a Python procedure fix_machine to take 2 string inputs
#               and returns the 2nd input string as the output if all of its
#               characters can be found in the 1st input string and "Give me
#               something that's not useless next time." if it's impossible.
#               Letters that are present in the 1st input string may be used
#               as many times as necessary to create the 2nd string (you
#               don't need to keep track of repeat usage).
#               For 5 gold stars, try solving this in one line.
#
# Author:      Akshay
#
# Created:     14-05-2015
#-------------------------------------------------------------------------------

def fix_machine(debris, product):
    """
    Takes two lists as inputs and returns the second list if all element of
    the second list are contained in the first (repeats not counted).
    Otherwise returns string 'Give me something that's not useless next time.'
    """
    return (product if (set(product).issubset(set(debris))) else "Give me something that's not useless next time.")

def test():
    print "Test case 1: ", fix_machine('UdaciousUdacitee', 'Udacity') == "Give me something that's not useless next time."
    print "Test case 2: ", fix_machine('buy me dat Unicorn', 'Udacity') == 'Udacity'
    print "Test case 3: ", fix_machine('AEIOU and sometimes y... c', 'Udacity') == 'Udacity'
    print "Test case 4: ", fix_machine('wsx0-=mttrhix', 't-shirt') == 't-shirt'

if __name__ == '__main__':
    test()
