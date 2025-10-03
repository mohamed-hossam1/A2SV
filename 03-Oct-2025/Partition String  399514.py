# Problem: Partition String  - https://leetcode.com/problems/partition-string/description/

class Solution:
    def partitionString(self, s: str) -> List[str]:
        l=[]
        st=""
        sts=set()
        for i in s:
            st+=i
            if(st not in sts):
                l.append(st)
                sts.add(st)
                st=""
        return l