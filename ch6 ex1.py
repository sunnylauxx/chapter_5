import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)





def turn_clockwise(direction):
    if direction == "N":
        return"E"
    elif direction == "E":
        return"S"
    elif direction == "S":
        return"W"
    elif direction == "W":
        return"W"
    
 
print("\nto_secs")
test(to_secs(2, 30, 10) == 9010)
test(to_secs(2, 0, 0) == 7200)
test(to_secs(0, 2, 0) == 120)
test(to_secs(0, 0, 42) == 42)
test(to_secs(0, -10, 10) == -590)

    
def to_sec(hours, minutes, seconds):
    
    sec_hour = hours * 60 * 60
    sec_min = minutes * 60
    return sec_hour + sec_minutes + seconds


