# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        count = 0
        j = 0
        for i in range(len(players)):
            while j<len(trainers) and trainers[j]<players[i]:
                j+=1
            if j==len(trainers):
                break
            count+=1
            j+=1
        return count
