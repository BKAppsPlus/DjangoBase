from math import sqrt


def min_dist_circle( x, y):
    # The shortest distance from any given point in the plane from the
    # perimeter of the circle is equal to the (shortest) distance of
    # that point to the center minus the radius
    # the (shortest/direct) distance between the point Z(x,y) from point
    # A(a, b) is D = sqrt( pow((x-a),2) + pow((y-b),2) )
    # is r is the diameter of the circle around A(a, b) the (shortest/direct)
    # distance from point Z to the perimeter is D-r
    # in the case of a = b = 0  and r = 1
    # I am using abs function for when Z is inside the circle
    try:
        dist = abs((sqrt(pow(x, 2)+pow(y, 2))-1))
        return dist
    except Exception as e :
        print('function min_dist_circle error: ' + str(e))
    
        


def french_weeks(normal_weeks):
    # 1 Minute = 100 Seconds
    # 1 Hour = 100 Minutes,
    # 1 Day = 10 Hours,
    # 1 Week = 10 Days.
    # the new french week would be in the format of W.DHmmss meaning :
    # For example 12.345678 french week is:
    # 12 french weeks and 3 french day and 4 french hours and 56 french minutes and 78 french seconds
    #
    # seems like the Seconds, Minutes , Hours and Weeks have all changed
    # their meaning. we need a comon denominator to convert the numbers
    # I assume the only common concept (because I guess is hardest to change)
    # is a day that should be used as a common denominator:
    # 
    # normal_days = normal_weeks * 7
    # normal_hours = normal_days * 24
    # normal_minutes = normal_hours * 60
    # normal_seconds = normal_minutes * 60
    #
    # french_days = normal_days
    #
    # french_weeks = french_days / 10
    # french_hours  = french_days * 10
    # french_minutes = french_hours * 100
    # french_seconds = french_minutes * 100
    try:
        normal_days = normal_weeks * 7
        french_days = normal_days
        french_weeks_val = french_days / 10
        return french_weeks_val
    except Exception as e :
        print('function french_weeks error: ' + str(e))


def majority_gate(a, b, c, d):
    # assuming all parameters are boolean out of 2*2*2*2=16 outcomes,
    # the result of the function should be True if:
    # Scenario #1 - All 4 are true                            = (1/16)
    # Scenario #2 - Three of them are True: 4!/(3!*(4-3)!)    = (4/16)
    # Scenario #3 - Two of them are True: 4!/(2!*(4-2)!)      = (6/16)
    # Scenario #4 - 2 of them are True: 4!/(2!*(4-2)!)        = (6/16)
    # the result of the function should be False if:
    # Scenario #5 - Only one of them are True: 4!/(1!*(4-1)!) = (4/16)
    # Scenario #6 - all four values are False:                = (1/16)
    #
    # BUT We know that Scenario #1 and Scenario #2 are subsets are Scenario #3
    # So we can just check for Scenario #3
    # or we can use the boolean minimization of boolean statements :
    try:
        if isinstance(a, bool) and isinstance(b, bool) and isinstance(c, bool) and isinstance(d, bool):
            val = (a and b) or (a and c) or (a and d) or (b and c) or (b and d) or (c and d)
            return val
        else:
            raise Exception('a, b, c and d should all be boolean')
    except Exception as e :
        print('function majority_gate error: ' + str(e))
        

def find_first_duplicate(list_of_int):
    # start reading the list (set) from teh begining at index 0, and save each number 
    # in a new set called 'visited', while crawling the input list (array) I check the 
    # visited list to see if the new int exist in the ones I have already visited.
    # once found return the index of teh duplicate int (current index) and if not return -1.
    
    # Check the input to be of type list if not raise an erro
    try:
        if isinstance(list_of_int, list):
            visited = set()
            # looping through the list_of_int (index=i and each item=n)
            for i, n in enumerate(list_of_int):
                if isinstance(n, int):
                    if n in visited:
                        # return the index of the new item is visited before
                        return i
                    else:
                        # add the number to the visited list 
                        visited.add(n)
                else:
                    raise Exception('non int detected in list_of_int')
            return -1
        else:
            raise Exception('list_of_int should be an array')
    except Exception as e :
        print('function find_first_duplicate error: ' + str(e))
    




print(min_dist_circle('wd', 3.8))
print(min_dist_circle(3, 3.8))
print()
print(french_weeks('sdf'))
print(french_weeks(2))
print(french_weeks(0))
print()
print(majority_gate(True, False, True, False))
print(majority_gate(True, False, True, 2))
print()
print(find_first_duplicate([7,4,5,6,33,36,'e']))
print(find_first_duplicate(345))
print(find_first_duplicate([4]))
print(find_first_duplicate([4,4,2,4234,235,5]))
print(find_first_duplicate([4,254,4]))
print(find_first_duplicate([4,3,3]))
print(find_first_duplicate([4,3,346,67,234,4578,7,4,3]))

