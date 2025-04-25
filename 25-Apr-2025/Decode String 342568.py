# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        val = []
        i=0
        while(i<len(s)):
            if s[i].isdigit():
                tmp = []
                while s[i].isdigit():
                    tmp.append(s[i])
                    i+=1
                i-=1
                val.append(int("".join(tmp)))
            else:
                if s[i]==']':
                    tmp = []
                    while stack[-1]!='[':
                        tmp.append(stack[-1])
                        stack.pop()
                    stack.pop()
                    tmp = tmp[::-1]*val[-1]
                    val.pop()
                    stack.extend(tmp)
                else:
                    stack.append(s[i])
            i+=1
        return("".join(stack))