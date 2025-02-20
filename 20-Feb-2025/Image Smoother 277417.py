# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        r, c = len(img), len(img[0])
        ans = [[0] * c for _ in range(r)]

        for i in range(r):
            for j in range(c):
                total_sum = 0
                count = 0

                for x in range(max(0, i-1), min(r, i+2)):
                    for y in range(max(0, j-1), min(c, j+2)):
                        total_sum += img[x][y]
                        count += 1

                ans[i][j] = total_sum // count

        return ans