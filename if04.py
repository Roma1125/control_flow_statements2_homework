def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    if a==b:
        s=0
    elif a>b:
        s=a
    elif b>a:
        s=b
    return s
print (main(2,2))
