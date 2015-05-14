#-------------------------------------------------------------------------------
# Name:        days_old.py
# Purpose:     Find the number of days between two legitimate dates.
#
# Author:      Akshay
#
# Created:     14-05-2015
#-------------------------------------------------------------------------------


days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(y):
    """
    Returns bool indicating whether y is a leap year.
    """
    if(y%4 != 0):
        return False
    else:
        if(y%100 != 0):
            return True
        else:
            if(y%400 != 0):
                return False
            else:
                return True

def num_of_days_from_first_jan(d,m,y):
    """
    Number of days from Jan 1 of the year y till that day. m is 0-11
    """
    days = 0
    for i in range(m):
        if(i == 1 and is_leap(y)):
            days = days + 1
        days = days + days_per_month[i]
    days = days + d
    return days


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Finds the number of days between (year1, month1, day1) and (year2, month2, day2)
    Assumes the second date is after the first and both dates are legitimate.
    """
    month1 = month1 - 1 #months are 0-11
    month2 = month2 - 1
    assert(day1 >= 0 and day1 <= days_per_month[month1])
    assert(day2 >= 0 and day2 <= days_per_month[month1])
    assert(month1 >= 0 and month1 < 12)
    assert(month2 >= 0 and month2 < 12)
    assert(year1 >= 0)
    assert (year2 >= year1)
    if(year2 == year1):
        assert(month2 >= month1)
        if(month2 == month1):
            assert(day2 >= day1)
    l = [(year1 + y) for y in range(year2 - year1)]
    ans = 0
    for y in l:
        ans = ans + 365
        if is_leap(y):
            ans = ans + 1
    ans = ans + num_of_days_from_first_jan(day2,month2,year2)
    ans = ans - num_of_days_from_first_jan(day1,month1, year1)
    return ans

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"


if __name__ == '__main__':
    test()
