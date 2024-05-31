class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        for (int num: nums) {
            String numToString = Integer.toString(num);
            if (numToString.length() % 2 == 0) {
                count++;
            }
        }
        
        return count;
    }
}