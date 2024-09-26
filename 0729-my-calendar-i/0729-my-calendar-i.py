class MyCalendar:

    def __init__(self):
        self.calender=[]
        

    def book(self, start: int, end: int) -> bool:
        for s,e in self.calender:
            if s < end and e > start:
                return False
        self.calender.append((start,end))
        return True


        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)