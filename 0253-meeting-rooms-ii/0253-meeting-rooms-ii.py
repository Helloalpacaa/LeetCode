class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        for interval in intervals:
            start.append(interval[0])
            end.append(interval[1])
        
        start.sort()
        end.sort()
        
        j = 0
        meetingRooms = 0
        for i in range(len(start)):
            if start[i] < end[j]:
                meetingRooms += 1
            else:
                j += 1
        
        return meetingRooms