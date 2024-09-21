class Solution {
    int[] father;

    public boolean validPath(int n, int[][] edges, int source, int destination) {
        init(n);
        join(edges);
        return find(source) == find(destination);
    }

    private void init(int n) {
        father = new int[n];
        for (int i = 0; i < n; i++) {
            father[i] = i;
        }
    }

    private void join(int[][] edges) {
        for (int[] edge: edges) {
            int u = find(edge[0]);
            int v = find(edge[1]);
            if (u != v) {
                father[v] = u;
            }
        }
    }

    private int find(int u) {
        if (u == father[u]) {
            return u;
        } else {
            father[u] = find(father[u]); //这里不能直接return father[u]，因为在join的过程中，father[u]的值可能会发生变化
            // 比如说example 1，如果把顺序改变成[[0,1],[2,0],[1,2]]
            // 那么1的根一开始是0，然后0的根变成了2，之后再遇到1时，需要去找它当前father也就是0最新的根 - 2,并且更新1的根为2
            return father[u];
        }
    }
}