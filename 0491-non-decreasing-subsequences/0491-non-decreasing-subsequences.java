class Solution {
    List<Integer> path = new LinkedList<>();
    List<List<Integer>> ans = new ArrayList<>();
    
    public List<List<Integer>> findSubsequences(int[] nums) {
        backtracking(nums, 0);
        return ans;
    }
    
    private void backtracking(int[] nums, int startIdx) {
        if (path.size() >= 2) {
            ans.add(new ArrayList<>(path));
        }
        
        Set<Integer> used = new HashSet<>();
        
        for (int i = startIdx; i < nums.length; i++) {
            if (path.size() > 0 && nums[i] < path.get(path.size() - 1) || used.contains(nums[i])) {
                continue;
            }
            
            path.add(nums[i]);
            used.add(nums[i]);
            backtracking(nums, i + 1);
            path.removeLast();
        }
    }
}