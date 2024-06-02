class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda a:(a[0], -a[1]))
        
        count = 0;
        
        for i in range(1, len(intervals)):
            if intervals[i][1] <= intervals[i - 1][1]:
                intervals[i][1] = intervals[i - 1][1]
                count += 1
        
        return len(intervals) - count