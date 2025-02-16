class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int right = piles[0];
        for (int pile: piles) {
            right = Math.max(right, pile);
        }

        int left = 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            int hour = 0;
            for (int pile: piles) {
                hour += Math.ceil((double) pile / mid);
            }
            if (hour <= h) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}