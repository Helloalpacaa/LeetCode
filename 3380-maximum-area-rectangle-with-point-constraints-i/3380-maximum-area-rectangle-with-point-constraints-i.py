class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:(x[0], x[1]))
        maxArea = -1
        print(points)

        for i in range(len(points) - 3):
            # 先找到长方形的第一条边, points[i][0] == points[i + 1][0]
            # 我们要找到第二条边，points[j][0] > points[i][0], points[j][0] == points[j + 1][0]
            # points[j][1] == points[i][1], points[j + 1][1] == points[i + 1][1]
            if points[i + 1][0] != points[i][0]:
                continue
            
            for j in range(i + 2, len(points) - 1):
                # 重点：先找到一个在第一条边的边界里的点，如果这个点不能组成长方形，那么这个点一定会在这条边之后形成的长方形的边界里，要break
                if points[i][1] <= points[j][1] <= points[i + 1][1]:
                    if points[j][0] == points[j + 1][0] and points[j][1] == points[i][1] and points[j + 1][1] == points[i + 1][1]:
                        maxArea = max(maxArea, (points[j][0] - points[i][0]) * (points[i + 1][1] - points[i][1]))
                    else:
                        break
        
        return maxArea
                
