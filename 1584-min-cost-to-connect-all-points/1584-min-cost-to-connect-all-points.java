class Solution {
    public int minCostConnectPoints(int[][] points) {
        Set<Integer> visit = new HashSet<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        pq.add(new int[] {0, 0}); // length, node index
        int ans = 0;

        while (visit.size() < points.length) {
            int[] node = pq.poll();
            if (visit.contains(node[1])) {
                continue;
            }
            ans += node[0];
            visit.add(node[1]);
            for (int i = 1; i < points.length; i++) {
                if (!visit.contains(i)) {
                    int length = Math.abs(points[i][0] - points[node[1]][0]) + Math.abs(points[i][1] - points[node[1]][1]);
                    
                    pq.add(new int[]{length, i});
                }
            }
        }
        return ans;
    }
}