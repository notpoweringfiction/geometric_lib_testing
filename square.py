def area(a):
    '''
        Returns area of square with given float side a

        Arguments:
            a (float): side of the square
    
        Returns:
            a * a (float): area of square from given side a
    '''

    if (a < 0): raise ValueError

    return a * a


def perimeter(a):
    '''
        Returns perimeter of square with given float side a

        Arguments:
            a (float): side of the square
    
        Returns:
            4 * a (float): perimeter of square with given side a
    '''
    if (a < 0): raise ValueError

    return 4 * a

