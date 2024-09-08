class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        def search(startRow, endRow, startCol, endCol) -> bool:
            if startRow >= endRow or startCol >= endCol:
                return False
            
            row = (endRow - startRow) // 2
            col = (endCol - startCol) // 2
            medium = matrix[row][col]

            if medium == target:
                return True
            elif medium < target:
                return search(startRow, row, startCol, col + 1) or search(row, row + 1, startCol, col)
            else:
                return search(startRow, row + 1, col + 1, endCol) or search(row + 1, endRow, startCol, endCol)

        
        return search(0, m, 0, n)
        