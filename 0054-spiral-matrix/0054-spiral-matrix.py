class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, n
        top, bottom = 0, m

        ans = []
        while len(ans) < m * n:
            for col in range(left, right):
                ans.append(matrix[top][col])
            top += 1

            for row in range(top, bottom):
                ans.append(matrix[row][right - 1])
            right -= 1
            
            if top < bottom:
                for col in range(right - 1, left - 1, -1):
                    ans.append(matrix[bottom - 1][col])
                bottom -= 1
            
            if left < right:
                for row in range(bottom - 1, top - 1, -1):
                    ans.append(matrix[row][left])
                left += 1
        
        return ans