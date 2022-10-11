def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Use the elif statments.
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"
    Args:
        temp: Temperature in Celsius.
    Returns:
        str: return answer.
    """
    if 0<temp<11:
        s="Very Cold"
    elif temp<0:
        s="Freezing"
    elif 10<temp<21:
        s="Cold"
    elif 20<temp<31:
        s="Normal"
    elif 30<temp<41:
        s="Hot"
    elif temp>40:
        s="Very Hot"
    return s
print (main(60))