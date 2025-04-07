# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        l = list(map(ord,s))
        shifts.sort()
        arr = [0]*(len(s)+1)
        for i , j , k in shifts :
            if k == 0 :
                arr[i] -= 1
                arr[j+1] +=1
            else :
                arr[i] +=1
                arr[j+1] -=1
        v = 0 
        for i in range(len(s)):
            v = v + arr[i]
            l[i] = 97 +(l[i] + v - 97)%26
        return ''.join(list(map(chr,l)))