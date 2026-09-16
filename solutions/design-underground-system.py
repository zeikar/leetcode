class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.timeSum = {}
        self.cnt = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkin.pop(id)
        key = (startStation, stationName)
        self.timeSum[key] = self.timeSum.get(key, 0) + t - startTime
        self.cnt[key] = self.cnt.get(key, 0) + 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        return self.timeSum[key] / self.cnt[key]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
