class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        def search(startRow, endRow, startCol, endCol) -> bool:
            if startRow >= endRow or startCol >= endCol:
                return False
            
            midRow = (startRow + endRow) // 2
            midCol = (startCol + endCol) // 2
            medium = matrix[midRow][midCol]

            if medium == target:
                return True
            elif medium < target:
                # Search bottom-left and top-right quadrants
                return search(midRow + 1, endRow, startCol, endCol) or \
                       search(startRow, midRow + 1, midCol + 1, endCol)
            else:
                # Search top-left and bottom-right quadrants
                return search(startRow, midRow, startCol, endCol) or \
                       search(midRow, endRow, startCol, midCol)

        
        return search(0, m, 0, n)
        