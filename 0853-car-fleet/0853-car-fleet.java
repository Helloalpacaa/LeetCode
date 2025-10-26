class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        if (position.length == 1) {
            return 1;
        }

        int[][] combine = new int[position.length][2];
        for (int i = 0; i < position.length; i++) {
            combine[i][0] = position[i];
            combine[i][1] = speed[i];
        }
        Arrays.sort(combine, (a, b) -> b[0] - a[0]);
        
        Deque<Double> stack = new ArrayDeque<>();
        for (int i = 0; i < combine.length; i++) {
            double time = (double) (target - combine[i][0]) / combine[i][1]; // time to arrive the target
            if (!stack.isEmpty() && time <= stack.peek()) {
                continue;
            } else {
                stack.push(time);
            }
        }
        return stack.size();
    }
}