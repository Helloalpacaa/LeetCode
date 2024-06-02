class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda a: a[0])
        
        ans = []
        left = intervals[0][0]
        right = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= right:
                left = min(left, intervals[i][0])
                right = max(right, intervals[i][1])
            else:
                ans.append([left, right])
                left = intervals[i][0]
                right = intervals[i][1]
        
        ans.append([left, right])
        
        return ans