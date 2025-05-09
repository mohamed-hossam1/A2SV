# Problem: My Calendar I - https://leetcode.com/problems/my-calendar-i/description/

class MyCalendar:

    def __init__(self):
        self.event = []

    def book(self, startTime: int, endTime: int) -> bool:
        for start,end in self.event:
            if (start <=startTime < end) or (startTime<=start and endTime>start):
                return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)