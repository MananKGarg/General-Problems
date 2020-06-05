def ispow2(n): # Check if a number is power of 2
    if (n == 0):
        return False
    elif (n ==1):
        return False
    while (n != 1):
        if(n % 2 != 0):
            return  False
        n = n // 2
    return True

def no2(n):     # If it is power of 2, then what power.

    count = 0
    while(n != 1 ):
        n = n//2
        count += 1
    return count














