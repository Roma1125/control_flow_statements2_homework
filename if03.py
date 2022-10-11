def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if c<a<b or b<a<c:
        answer=a
    elif c<b<a or a<b<c:
        answer=b
    elif b<c<a or a<c<b:
        answer=c
    return answer
print (main (1,2,3)) 