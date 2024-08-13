class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int total = 0;
        int subTotal = 0;
        int startIdx = 0;
        for (int i = 0; i < gas.length; i++) {
            subTotal += (gas[i] - cost[i]);
            total += (gas[i] - cost[i]);
            if (subTotal < 0) {
                startIdx = i + 1;
                subTotal = 0;
            }
        }
        if (total < 0) {
            return -1;
        }
        return startIdx;
    }
}