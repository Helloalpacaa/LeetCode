class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        arrows = 1
        
        for i in range(1, len(points)):
            if points[i][0] <= points[i - 1][1]:
                points[i][1] = min(points[i - 1][1], points[i][1])
            else:
                arrows += 1
        
        return arrows