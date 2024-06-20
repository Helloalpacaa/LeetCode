class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        count = len(intervals)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[i - 1][0] and intervals[i][1] <= intervals[i - 1][1]:
                count -= 1
                intervals[i][0] = intervals[i - 1][0]
                intervals[i][1] = intervals[i - 1][1]
        
        return count