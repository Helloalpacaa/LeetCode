class Solution {
    int[] father;

    public boolean validTree(int n, int[][] edges) {
        // A valid tree must have exactly n-1 edges
        if (edges.length != n - 1) {
            return false;
        }

        init(n);
        for (int[] edge: edges) {
            int u = find(edge[0]);
            int v = find(edge[1]);

            // If two nodes have the same root, a cycle exists
            if (u == v) {
                return false;
            }
            join(u, v);
        }
        
        // 之前在这里check了是否father[i]都是同一个值
        // 不需要，因为已经在第一步check了the number of edges and cycles

        return true;
    }

    private void init(int n) {
        father = new int[n];
        for (int i = 0; i < n; i++) {
            father[i] = i;
        }
    }

    private void join(int u, int v) {
        u = find(u);
        v = find(v);
        if (u != v) {
            father[v] = u;
        }
    }

    private int find(int u) {
        if (u == father[u]) {
            return u;
        } else {
            father[u] = find(father[u]);
            return father[u];
        }
    }
}