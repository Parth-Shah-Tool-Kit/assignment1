#Given an string x, return true if x is a palindrome, and false otherwise

def Palindrome(s):
    return s == s[::-1]
 
x = int(input("Enter the number to be checked: "))

check = Palindrome(str(x))
print(check)
