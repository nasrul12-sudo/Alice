import time

def seccond():
    sec = time.time()
    return sec

class TimeManagement:
    def __init__(self, sec):
        self.sec = sec

    def now(self):
        localTime = time.ctime(self.sec)
        return localTime
    
    def birthday(self):
        result = time.localtime(self.sec)
        day = result.tm_mday
        mount = result.tm_mon
        
        return day, mount


# MyTime = TimeManagement(seccond())
# now = MyTime.now()
# print(now)

# birth = MyTime.birthday()