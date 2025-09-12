# Problem: Minimum One Bit Operations to Make Integers Zero - https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/description/?envType=problem-list-v2&envId=bit-manipulation

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # helper fuction 
        def helper(x) :
            mapper = {0:0,1:1,2:3,3:2}
            if x in mapper :
                return mapper[x]
            else:
                k = (int)(math.log(x,2))
                main = (2**(k+1))-1
                residue =  x - (2**k)
                return main - helper(residue)

        ans = helper(n)
        return ans
        