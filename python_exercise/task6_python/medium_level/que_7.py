# Write a Python program to check if a number is a power of two using recursion.
def isPowerOfTwo(n):
    if (n == 0):
        return False
    while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
             
    return True
 
if(isPowerOfTwo(31)):
    print('Yes')
else:
    print('No')