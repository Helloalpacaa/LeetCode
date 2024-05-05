class Solution {
    private List<Integer> path = new LinkedList<>();
    private List<List<Integer>> ans =  new ArrayList<>();
    
    public List<List<Integer>> combinationSum3(int k, int n) {
        backtracking(k, 0, n, 1);
        return ans;
    }
    
    private void backtracking(int k, int sum, int targetSum, int number) {
        if (path.size() == k) {
            if (sum == targetSum) {
                ans.add(new ArrayList<>(path));
            }
            return;
        }
        
        for (int i = number; i <= 9 - (k - path.size()) + 1; i++) {
            if (sum > targetSum) {
                break;
            }
            
            sum += i;
            path.add(i);
            backtracking(k, sum, targetSum, i + 1);
            sum -= i;
            path.removeLast();
        }
    }
}