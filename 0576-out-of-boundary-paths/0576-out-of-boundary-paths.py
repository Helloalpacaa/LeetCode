class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove < 0:
            return 0
        
        # 如果当前position不在boundry内，说明找到了一条valid path，return 1
        if not (0 <= startRow < m and 0 <= startColumn < n):
            return 1

        return (self.findPaths(m, n, maxMove - 1, startRow, startColumn - 1) + 
                self.findPaths(m, n, maxMove - 1, startRow, startColumn + 1) + 
                self.findPaths(m, n, maxMove - 1, startRow - 1, startColumn) + 
                self.findPaths(m, n, maxMove - 1, startRow + 1, startColumn)) % 1000000007
        
