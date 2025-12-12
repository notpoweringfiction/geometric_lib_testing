def area(a, h): 
    '''
        Returns area of right triangle based from integer cathetus and float height (other cathetus)

        Arguments:
            a (float): cathetus of triangle, different from height h
            h (float): second side, which is different from cathetus a
    
        Returns:
            a * h / 2 (float): area of right triangle with cathetus a and height h
    '''
    return a * h / 2 

def perimeter(a, b, c): 
    '''
        Returns perimeter of triangle from all 3 different cathetus floats (triangle sides)

        Arguments:
            a (float): first side, which is different to b and c argument
            b (float): second side, which is different to a and c argument
            c (float): third side of triangle, which is different to b and a argument
    
        Returns:
            a + b + c (float): perimeter of triangle with sides a, b and c
    '''
    return a + b + c 
