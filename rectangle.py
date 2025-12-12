def area(a, b): 
    '''
        Returns area of rectangle with given adjacent float sides a, b

        Arguments:
            a (float): first side
            b (float): second side, which is adjacent to previous argument
    
        Returns:
            a * b (float): area of rectangle with adjacent sides a, b
    '''
    if (a < 0 or b < 0): raise ValueError

    return a * b 

def perimeter(a, b): 
    '''
        Returns perimeter of rectangle with given adjacent float sides a, b

        Arguments:
            a (float): first side
            b (float): second side, which is adjacent to previous argument
    
        Returns:
            (a + b) * 2 (float): perimeter of rectangle with adjacent sides a, b
    '''
    if (a < 0 or b < 0): raise ValueError

    return (a + b) * 2 
