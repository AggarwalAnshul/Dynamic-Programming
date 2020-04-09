def hcf(a, b):
    if b == 0:
        return a
    return hcf(b, a % b)

def reduceFraction(x, y):
    while hcf(x, y) > 1:
        factor = hcf(x, y)
        x /= factor
        y /= factor
    return (x, y)
    
print(reduceFraction(0, 5))