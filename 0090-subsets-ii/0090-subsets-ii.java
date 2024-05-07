class Solution {
    List<Integer> path = new LinkedList<>();
    List<List<Integer>> ans = new ArrayList<>();
    
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        backtracking(nums, 0);
        return ans;
    }
    
    private void backtracking(int[] nums, int startIdx) {
        ans.add(new ArrayList<>(path));
        
        for (int i = startIdx; i < nums.length; i++) {
            if (i > startIdx && nums[i] == nums[i - 1]) {
                continue;
            }
            
            path.add(nums[i]);
            backtracking(nums, i + 1);
            path.removeLast();
        }
    }
}