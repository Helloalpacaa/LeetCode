class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        for interval in intervals:
            start.append(interval[0])
            end.append(interval[1])
        start.sort()
        end.sort()

        rooms = 0
        j = 0
        for i in range(len(start)):
            if start[i] < end[j]:
                rooms += 1
            else:
                j += 1
        
        return rooms