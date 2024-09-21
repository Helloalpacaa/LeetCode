class Solution {
    private int[] father;
    public int[] findRedundantDirectedConnection(int[][] edges) {
        father = new int[edges.length + 1];
        int[] inDegree = new int[edges.length + 1];
        for (int i = 0; i < edges.length; i++) {
            inDegree[edges[i][1]]++; // 计算出每个node被指向的次数
        }

        // 找到被指向次数为2的edge在edges里的index，从后往前，因为优先返回最后出现的edge
        ArrayList<Integer> twoDegree = new ArrayList<>();
        for (int i = edges.length - 1; i >= 0; i--) {
            if (inDegree[edges[i][1]] == 2) {
                twoDegree.add(i);
            }
        }

        // 处理两种情况，一种是某个节点被指向次数为2，需要删掉其中一条边，另一种情况是每个节点被指向次数都为1，但是行成了circle
        // 如果是某个节点被指向次数为2，看删掉哪条依然能构成树
        if (!twoDegree.isEmpty()) {
            // 优先检查第一条边，因为第一条边的index要大一些，如果第一条边不满足条件那么肯定是第二条边
            if (isTreeAfterRemoveEdge(edges, twoDegree.get(0))) {
                return edges[twoDegree.get(0)];
            }
            return edges[twoDegree.get(1)];
        }

        // 如果是第二种情况，找到组成构成circle的edge
        return getRemoveEdge(edges);
    }

    private void init(int n) {
        for (int i = 1; i <= n; i++) {
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
        return u == father[u] ? u : (father[u] = find(father[u]));
    }

    private Boolean same(int u, int v) {
        return find(u) == find(v);
    }

    private boolean isTreeAfterRemoveEdge(int[][] edges, int deleteEdge) {
        init(edges.length);
        for (int i = 0; i < edges.length; i++) {
            if (i == deleteEdge) {
                continue;
            }
            if (same(edges[i][0], edges[i][1])) { // 如果不加入deleteEdge来建造一个graph，却还是有circle，说明这条删除这条deleteEdge无法解决问题
                return false;
            }
            join(edges[i][0], edges[i][1]);
        }
        return true;
    }

    private int[] getRemoveEdge(int[][] edges) {
        init(edges.length);
        for (int i = 0; i < edges.length; i++) {
            if (same(edges[i][0], edges[i][1])) {
                return edges[i];
            }
            join(edges[i][0], edges[i][1]);
        }
        return null;
    }
}