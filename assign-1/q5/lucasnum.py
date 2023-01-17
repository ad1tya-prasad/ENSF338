
# Lucas number definition
def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    if n > 1:
        return lucas(n-2) + lucas(n-1)	

if __name__ == '__main__': 
    # Test for n = 0 and n = 1 
    print("The 0th Lucas number is", lucas(0))
    print("The 1st Lucas number is", lucas(1))
    # Test for n = 2
    print("The 2nd Lucas number is", lucas(2))