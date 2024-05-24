class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int[] ans = new int[nums.length];
        Arrays.fill(ans, -1);
        Deque<Integer> stack = new ArrayDeque<>();
        
        for (int i = 0; i < nums.length * 2; i++) {
            while (!stack.isEmpty() && nums[i % nums.length] > nums[stack.peek()]) {
                ans[stack.peek()] = nums[i % nums.length];
                stack.pop();
            }
            stack.push(i % nums.length);
        }
        
        return ans;
    }
}