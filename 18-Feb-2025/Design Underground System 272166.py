# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem(object):

    def __init__(self):
        self.inData = defaultdict(list)
        self.average = defaultdict(list)


    def checkIn(self, id, stationName, t):
        self.inData[id] = [stationName,t]
        

    def checkOut(self, id, stationName, t):
        inName,inT = self.inData[id]
        self.average[(inName,stationName)].append(t-inT)
        

    def getAverageTime(self, startStation, endStation):
        sum = float()
        lst = self.average[(startStation,endStation)]
        for i in lst:
            sum+=i
        return sum/len(lst)
        
        
