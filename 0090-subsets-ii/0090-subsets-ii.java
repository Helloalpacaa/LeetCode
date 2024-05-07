class Solution {
    List<Integer> path = new LinkedList<>();
    Set<List<Integer>> ans = new HashSet<>();
    
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        backtracking(nums, 0);
        return new ArrayList<>(ans);
    }
    
    private void backtracking(int[] nums, int startIdx) {
        ans.add(new ArrayList<>(path));
        
        for (int i = startIdx; i < nums.length; i++) {
            path.add(nums[i]);
            backtracking(nums, i + 1);
            path.removeLast();
        }
    }
}