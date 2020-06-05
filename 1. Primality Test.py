def isprime(n):   # n is a natural number greater than 1

    if ((n == 2) or (n == 3)):
        return True
    else:
        if ((n % 2 == 0) or (n % 3 == 0)): # We do this so that we can increment by 6 later on
            return False
        else:
            i = 5   # first 6*k - 1
            while i*i <= n:  # Check only till sqrt(n)
                if ((n % i == 0) or (n % (i+2) == 0)): # check by 6*k - 1 and 6*k + 1
                    return False
                i += 6
        return True  # If nothing divides n, it is infact prime

