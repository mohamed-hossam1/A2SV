# Problem: Gray Code - https://leetcode.com/problems/gray-code/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        total = 2 ** n
        path = [0]
        answer = []
        def bt(taken):
            if len(path) == 2 ** n and (path[-1] ^ path[0]).bit_count() == 1:
                answer.append(path)
                return True

            for bit in range(n):
                num = path[-1] ^ (1 << bit)
                if num not in taken:
                    taken.add(num)
                    path.append(num)
                    if bt(taken):
                        return True

                    taken.remove(num)
                    path.pop()
            
            return False

        bt(set([0]))

        return answer[0]

