def extraLongFactorials(n):
    # Write your code here
    if n == 0:
        return 1
    else:
        return n * extraLongFactorials(n-1)
        

print(extraLongFactorials(25))