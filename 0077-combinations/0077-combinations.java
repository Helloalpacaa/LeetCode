class Solution {
    private List<Integer> path = new LinkedList<>();
    private List<List<Integer>> ans = new ArrayList<>();
    
    public List<List<Integer>> combine(int n, int k) {
        backtracking(n, k, 1);
        return ans;
    }
    
    private void backtracking(int n, int k, int startIdx) {
        if (path.size() == k) {
            ans.add(new ArrayList<>(path));
            return;
        }
        
        for (int i = startIdx; i <= n; i++) {
            path.add(i);
            backtracking(n, k, i + 1);
            path.removeLast();
        }
    }
}