class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        int max = 1;
        int newMax = 1;
        int ans = nums[0];
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                max++;
                if (max > newMax) {
                    newMax = max;
                    ans = nums[i];
                }
            } else {
                max = 1;
            }
        }
        return ans;
    }
}