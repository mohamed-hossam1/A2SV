# Problem: Find geometric sum of the series using recursion - https://www.geeksforgeeks.org/find-geometric-sum-of-the-series-using-recursion/

def sum(n):
    
    if n == 0:
        return 1
    ans =  1 / pow(3, n)

    return ans+ sum(n-1)