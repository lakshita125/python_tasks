#QUE.6 Implement a function to check if an array is a palindrome (reads the same forwards and backwards).

def isPalindrome(s):
    return s == s[::-1]
 
s = [1,2,3,4,1]
output= isPalindrome(s)
 
if output:
    print("Yes")
else:
    print("No")