import math


def area(r):
    '''
        Returns area of circle with given float radius
        
        Arguments:
            r (float): radius
    
        Returns:
            math.pi * r * r (float): area of circle with radius r
    '''
    return math.pi * r * r


def perimeter(r):
    '''
        Returns perimeter of circle with given float radius
    
        Arguments:
            r (float): radius
    
        Returns:
            2 * math.pi * r (float): perimeter of circle with radius r
            '''
    return 2 * math.pi * r
