# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet(object):

    def __init__(self):
        self.s = set()

    def insert(self, val):
        if val in self.s:
            return False
        self.s.add(val)
        return True
        

    def remove(self, val):
        if val in self.s:
            self.s.remove(val)
            return True
        return False
        

    def getRandom(self):
        if not self.s:
            return None
        return random.choice(tuple(self.s)) 
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()