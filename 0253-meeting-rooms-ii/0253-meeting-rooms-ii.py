class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # start : [0, 5, 15]
        # end:    [10,20,30]
        start = []
        end = []
        for s, e in intervals:
            start.append(s)
            end.append(e)
        
        start.sort()
        end.sort()
        i, j = 0, 0
        count = 0
        while i < len(start):
            if start[i] < end[j]:
                count += 1
            else:
                j += 1
            i += 1
        
        return count
        