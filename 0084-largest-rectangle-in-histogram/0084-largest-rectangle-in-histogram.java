class Solution {
    public int largestRectangleArea(int[] heights) {
        int[] newHeights = new int[heights.length + 2];
        newHeights[0] = 0;
        for (int i = 0; i < heights.length; i++) {
            newHeights[i + 1] = heights[i];
        }
        newHeights[newHeights.length - 1] = 0;
        int largestRectangleArea = 0;
        
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < newHeights.length; i++) {
            while (!stack.isEmpty() && newHeights[i] < newHeights[stack.peek()]) {
                int height = newHeights[stack.pop()];
                int width = i - stack.peek() - 1;
                int area = height * width;
                largestRectangleArea = Math.max(area, largestRectangleArea);
            }
            stack.push(i);
        }
        
        return largestRectangleArea;
    }
}