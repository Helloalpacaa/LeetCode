class Solution {
    LinkedList<Integer> path = new LinkedList<>();
    List<List<Integer>> ans = new ArrayList<>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        backTracking(candidates, target, 0, 0);
        return ans;
    }

    private void backTracking(int[] candidates, int targetSum, int sum, int startIdx) {
        if (sum == targetSum) {
            ans.add(new ArrayList<>(path));
        }

        for (int i = startIdx; i < candidates.length; i++) {
            if (sum > targetSum) {
                break;
            }
            path.add(candidates[i]);
            sum += candidates[i];
            backTracking(candidates, targetSum, sum, i);
            sum -= candidates[i];
            path.removeLast();
        }
    }
}