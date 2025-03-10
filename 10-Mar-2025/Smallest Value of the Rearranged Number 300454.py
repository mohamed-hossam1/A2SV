# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num):
        x = []
        p = False
        num = str(num)
        if num[0]=='-':
            num = num[1:]
            p=True
        for i in range(len(num)):
            x.append(num[i])
        x.sort()
        ans = ''
        count = 0
        for i in x:
            if i == '0':
                count+=1
        if p:
            ans = '0'*count
            if count!=len(num):
                ans+= x[count] 
        else:
            if count!=len(num):
                ans = x[count] 
            ans +='0'*count
        for i in range(count+1,len(x)):
            ans+=x[i]
        if p:
            ans = '-'+ans[::-1]
        return int(ans)
        