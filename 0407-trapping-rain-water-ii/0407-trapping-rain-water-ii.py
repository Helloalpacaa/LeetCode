class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])
        heap = []
        visited = set()

        # Add all border cells to heap
        for col in range(0, n):
            heapq.heappush(heap, (heightMap[0][col], 0, col))
            heapq.heappush(heap, (heightMap[m - 1][col], m - 1, col))

        for row in range(0, m):
            heapq.heappush(heap, (heightMap[row][0], row, 0))
            heapq.heappush(heap, (heightMap[row][n - 1], row, n - 1))
        
        # max_height represents this "lowest boundary point" that we've encountered so far
        max_height = 0
        water = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # Process cells from lowest to highest height
        while heap:
            height, row, col = heapq.heappop(heap)
            visited.add((row, col))
            max_height = max(max_height, heightMap[row][col])

            for direction in directions:
                adj_row = row + direction[0]
                adj_col = col + direction[1]

                # Check if adjacent cell is valid and unvisited
                if 0 <= adj_row < m and 0 <= adj_col < n and (adj_row, adj_col) not in visited:
                    # If adjacent cell is lower than max_height, it can trap water
                    if heightMap[adj_row][adj_col] < max_height:
                        water += (max_height - heightMap[adj_row][adj_col])
                    
                    visited.add((adj_row, adj_col))
                    heapq.heappush(heap, (heightMap[adj_row][adj_col], adj_row, adj_col))
        
        return water
