# Problem: Convert a String to an Integer using Recursion - https://www.geeksforgeeks.org/convert-a-string-to-an-integer-using-recursion/

def stringToInt(str, index):
    if index == len(str):
        return 0

    digit = int(str[index])
    po = len(str) - index - 1

    return digit * (10 **po ) + stringToIntHelper(str, index + 1)