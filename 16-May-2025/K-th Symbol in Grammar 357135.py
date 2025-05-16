# Problem: K-th Symbol in Grammar - https://leetcode.com/problems/k-th-symbol-in-grammar/description/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        ls = [0]
        while n>1:
            tm = []
            for x in ls:
                if x==0:
                    tm.append(0)
                    tm.append(1)
                else:
                    tm.append(1)
                    tm.append(0)
            ls = tm
            n-=1
        return(ls[k-1])

        