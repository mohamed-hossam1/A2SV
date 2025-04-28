# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        
        A = [-10^12] + A + [-10^12]
        st = []
        ans = 0
        
        for i in range(len(A)):
            
            while st and A[st[-1]] > A[i]: 
                mid = st.pop()
                left = st[-1]
                right = i 
                
                ans+=A[mid]*(mid-left)* (right-mid)
            
            st.append(i)
        return ans %(10**9 + 7)