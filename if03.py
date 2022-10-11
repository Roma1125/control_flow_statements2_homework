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
    if c<b<a or b<c<a:
        answer=a
    elif c<a<b or a<c<b:
        answer=b
    else:
        answer = c
    return answer
print (main (5,8,3))