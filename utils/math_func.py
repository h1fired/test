def division(a, b):
    if type(a) not in [float, int] or type(b) not in [float, int]:
        raise TypeError
    
    return a / b