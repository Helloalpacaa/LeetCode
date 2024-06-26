class Solution {
    public int maximalRectangle(char[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[] height = new int[n + 1];
        int maximalRectangle = 0;
        Stack<Integer> stack = new Stack<>();
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '1') {
                    height[j]++;
                } else {
                    height[j] = 0;
                }
            }
            
            for (int j = 0; j <= n; j++) {
                while (!stack.isEmpty() && height[j] < height[stack.peek()]) {
                    int h = height[stack.pop()];
                    int w = stack.isEmpty() ? j : j - stack.peek() - 1;
                    int area = h * w;
                    maximalRectangle = Math.max(area, maximalRectangle);
                }
                stack.push(j);
            }
            stack.clear();
        }
        
        return maximalRectangle;
    }
}