def main(a,b,c):
#print("salom dunyo")
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b and a>c:
        s=a
    elif b>a and b>c:
        s=b
    elif c>a and c>b:
        s=c
    return s
print (main (1,2,3)) 
