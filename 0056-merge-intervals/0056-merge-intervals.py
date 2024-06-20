class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort(key = lambda x: x[0])
        
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[i - 1][0] and intervals[i][0] <= intervals[i - 1][1]:
                intervals[i][0] = min(intervals[i][0], intervals[i - 1][0])
                intervals[i][1] = max(intervals[i][1], intervals[i - 1][1])
            else:
                merged.append([intervals[i - 1][0], intervals[i - 1][1]])
        
        merged.append([intervals[len(intervals) - 1][0], intervals[len(intervals) - 1][1]])
        return merged