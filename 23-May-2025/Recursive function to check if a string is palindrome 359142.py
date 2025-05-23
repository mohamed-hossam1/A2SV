# Problem: Recursive function to check if a string is palindrome - https://www.geeksforgeeks.org/recursive-function-check-string-palindrome/

def palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    
    l = 0
    r = len(s)-1
    
    answer = palindrome(s[l+1:r]) and (s[l] == s[r])
    
    return answer