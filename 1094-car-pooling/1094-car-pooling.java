class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        int[] stop = new int[1001];
        
        for (int[] trip: trips) {
            stop[trip[1]] += trip[0];
            stop[trip[2]] -= trip[0];
        }
        
        int currPass = 0;
        for (int i = 0; i < stop.length; i++) {
            currPass += stop[i];
            if (currPass > capacity) {
                return false;
            }
        }
        
        return true;
    }
}