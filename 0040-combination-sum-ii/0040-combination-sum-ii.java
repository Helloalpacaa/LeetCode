class Solution {
    private List<Integer> path = new LinkedList<>();
    private List<List<Integer>> ans = new ArrayList<>();
    
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        backtracking(candidates, 0, target, 0);
        return ans;
    }
    
    private void backtracking(int[] candidates, int sum, int targetSum, int startIdx) {
        if (sum == targetSum) {
            ans.add(new ArrayList<>(path));
            return;
        }
        
        for (int i = startIdx; i < candidates.length; i++) {
            if (i > startIdx && candidates[i] == candidates[i - 1]) {
                continue;
            }
            
            if (sum > targetSum) {
                break;
            }
            
            sum += candidates[i];
            path.add(candidates[i]);
            backtracking(candidates, sum, targetSum, i + 1);
            path.removeLast();
            sum -= candidates[i];
        }
    }
}