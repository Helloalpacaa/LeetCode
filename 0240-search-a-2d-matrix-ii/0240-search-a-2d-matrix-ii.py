class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        # Medium of medium approch, the time complexity of this algorithm is O(n^log4(3)), not O(log n).
        # At each step, you're making two recursive calls, each on a problem size that's at most 3/4 of the original.
        # This leads to the recurrence relation: T(n) = 2T(3n/4) + O(1)
        # Solving this recurrence using the master theorem gives us O(n^log4(3)), which is approximately O(n^0.792).

        # def search(startRow, endRow, startCol, endCol) -> bool:
        #     if startRow >= endRow or startCol >= endCol:
        #         return False
            
        #     midRow = (startRow + endRow) // 2
        #     midCol = (startCol + endCol) // 2
        #     medium = matrix[midRow][midCol]

        #     if medium == target:
        #         return True
        #     elif medium > target:
        #         return search(startRow, midRow, startCol, endCol) or search(midRow, endRow, startCol, midCol)
        #     else:
        #         return search(startRow, endRow, midCol + 1, endCol) or search(midRow + 1, endRow, startCol, midCol + 1)

        
        # return search(0, m, 0, n)
        
        row = 0
        col = n - 1

        while row < m and col >= 0:
            val = matrix[row][col]
            if val == target:
                return True
            elif val > target:
                col -= 1
            else:
                row += 1
        
        return False