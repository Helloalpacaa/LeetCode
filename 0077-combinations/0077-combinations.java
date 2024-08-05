class Solution {
    List<List<Integer>> ans;
    LinkedList<Integer> path;
    public List<List<Integer>> combine(int n, int k) {
        ans = new ArrayList<>();
        path = new LinkedList<>();
        backTracking(n, k, 1);
        return ans;
    }

    private void backTracking(int n, int k, int index) {
        if (path.size() == k) {
            ans.add(new ArrayList<>(path));
            return;
        }

        // 已经选择的元素个数：path.size()
        // 还需要的元素个数为：k - path.size()
        // 在集合n中至多要从该起始位置：n - (k - path.size()) + 1，开始遍历
        // 例子1就不会有起始index为i = 4的情况，因为4后面没有数字，无论如何也凑不出一对组合
        for (int i = index; i <= n - (k - path.size()) + 1; i++) {
            path.add(i);
            backTracking(n, k, i + 1);
            path.removeLast();
        }
    }
}