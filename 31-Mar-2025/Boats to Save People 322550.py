# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        l,r = 0,len(people)-1
        count = 0
        while l<=r:
            if (people[l]+people[r])<=limit:
                l+=1
            r-=1
            count+=1
        return count