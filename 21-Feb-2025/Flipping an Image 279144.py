# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution(object):
    def flipAndInvertImage(self, image):

        for i in image:
            i.reverse()
            for c in range(len(i)):
                if i[c] == 1:
                    i[c]=0
                else:
                    i[c]=1
        return image


        