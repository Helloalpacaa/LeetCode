class UndergroundSystem:
    # check_in = {id: (stationName, t)}  
    # travel_data = {(startStation, endStation): [total_time, count]}

    def __init__(self):
        self.check_in = {}
        self.travel_data = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        check_in_station, check_in_time = self.check_in[id]
        time = t - check_in_time
        if (check_in_station, stationName) in self.travel_data:
            total_time, count = self.travel_data[(check_in_station, stationName)]
            self.travel_data[(check_in_station, stationName)] = (total_time + time, count + 1)
        else:
            self.travel_data[(check_in_station, stationName)] = (time, 1)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.travel_data[(startStation, endStation)]
        return total_time / count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)