def division(a, b):
    """ Division two numbers """
    if type(a) not in [float, int] or type(b) not in [float, int]:
        raise TypeError
    if b == 0: 
        raise ZeroDivisionError
    
    return a / b