# Check if a list is a palindrome
def isPalindrome(s):
    return s == s[::-1]
 
s = [1,2,3,4,1]
output= isPalindrome(s)
 
if output:
    print("Yes, the given list is palindrome")
else:
    print("No, the given list is not palindrome")