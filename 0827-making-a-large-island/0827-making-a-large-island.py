class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # 依然是在grid[i][j] == 1时去找它连接的island，然后把它们的数字改成2开始，因为原本的grid里只有0和1
        # 计算出这个岛的area，用一个hashmap存储每个mark的area
        # 再遍历一次grid，在每个为0的cell，加上它四周的island area，寻找最大area
        m = len(grid)
        n = len(grid[0])
        areaMap = {}
        visited = set()

        def getArea(i, j, mark) -> int:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or (i, j) in visited:
                return 0
            
            grid[i][j] = mark
            visited.add((i, j))
            return 1 + getArea(i + 1, j, mark) + getArea(i - 1, j, mark) + getArea(i, j + 1, mark) + getArea(i, j - 1, mark)
        
        mark = 2
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = getArea(i, j, mark)
                    maxArea = max(area, maxArea) # 以免没有为0的cell
                    areaMap[mark] = area
                    mark += 1
        
        
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    visited = set()
                    currArea = 1
                    for direction in directions:
                        next_i = i + direction[0]
                        next_j = j + direction[1]
                        if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] != 0 and grid[next_i][next_j] not in visited:
                            currArea += areaMap.get(grid[next_i][next_j])
                            visited.add(grid[next_i][next_j])
                    maxArea = max(currArea, maxArea)

        return maxArea