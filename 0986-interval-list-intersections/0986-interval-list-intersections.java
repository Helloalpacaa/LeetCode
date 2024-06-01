class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        int i = 0;
        int j = 0;
        List<int[]> list = new ArrayList<>();
        
        while (i < firstList.length && j < secondList.length) {
            int a1 = firstList[i][0];
            int a2 = firstList[i][1];
            int b1 = secondList[j][0];
            int b2 = secondList[j][1];
            
            if (b2 >= a1 && a2 >= b1) {
                list.add(new int[]{Math.max(a1, b1), Math.min(a2, b2)});
            }
            
            if (a2 < b2) {
                i++;
            } else {
                j++;
            }
        }
        
        int[][] ans = new int[list.size()][2];
        for (int index = 0; index < list.size(); index++) {
            ans[index] = list.get(index);
        }
        
        return ans;
    }
}