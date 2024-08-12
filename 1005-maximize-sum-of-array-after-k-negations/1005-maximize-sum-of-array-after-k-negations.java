class Solution {
    public int largestSumAfterKNegations(int[] nums, int k) {
        nums = IntStream.of(nums).boxed().sorted((a, b) -> Math.abs(b) - Math.abs(a))
        .mapToInt(Integer::intValue).toArray();
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < 0 && k > 0) {
                nums[i] = - nums[i];
                k--;
            }
        }

        if (k % 2 == 1) {
            nums[nums.length - 1] = - nums[nums.length - 1];
        }
        return Arrays.stream(nums).sum();
    }
}