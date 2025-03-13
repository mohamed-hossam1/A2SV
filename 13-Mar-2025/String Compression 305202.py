# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution(object):
    def compress(self, chars):
        if len(chars)==1:
            return 1
        i = 0
        ans = 0
        while i<len(chars):
            c = chars[i]
            count = 0
            while i<len(chars) and chars[i]==c:
                count+=1
                i+=1
            chars[ans] = c
            ans+=1
            if count>1:
                for x in str(count):
                    chars[ans] = x
                    ans+=1
        return ans

        