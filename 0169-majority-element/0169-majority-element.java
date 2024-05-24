class Solution {
    public int majorityElement(int[] nums) {
        int ans = 0;
        int count = 0;
        for (int num: nums) {
            if (count == 0) {
                ans = num;
            }
            count += (ans == num) ? 1 : -1;
        }
        return ans;
    }
}