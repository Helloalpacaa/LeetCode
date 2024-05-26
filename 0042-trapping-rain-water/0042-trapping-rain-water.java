class Solution {
    public int trap(int[] height) {
        int water = 0;
        Deque<Integer> stack = new ArrayDeque<>();
        
        for (int i = 0; i < height.length; i++) {
            while (!stack.isEmpty() && height[i] > height[stack.peek()]) {
                int base = height[stack.pop()];
                if (!stack.isEmpty()) {
                    int left = stack.peek();
                    int area = (Math.min(height[i], height[left]) - base) * (i - left - 1);
                    water += area;
                }
            }
            stack.push(i);
        }
        
        return water;
    }
}