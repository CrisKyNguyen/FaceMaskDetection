import time

class Fps():
    def __init__(self) -> None:
        self.preTime:float = time.time()
    
    def next(self) -> int:
        newTime:float = time.time()
        fps = 1/(newTime - self.preTime)
        self.preTime = newTime
        return int(round(fps))

    def nextStr(self) -> str:
        return str(self.next())