class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        ArrayList<Integer>[] pre = new ArrayList[numCourses];
        for (int i = 0; i < numCourses; i++) {
            pre[i] = new ArrayList<>();
        }

        for (int[] prerequisity: prerequisites) {
            pre[prerequisity[0]].add(prerequisity[1]);
        }

        int[] state = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
            if (isCircle(pre, i, state)) {
                return false;
            }
        }
        return true;
    }

    private boolean isCircle(ArrayList<Integer>[] pre, int i, int[] state) {
        if (state[i] == 1) {
            return true;
        }

        if (state[i] == 2) {
            return false;
        }

        state[i] = 1;
        for (int course: pre[i]) {
            if (isCircle(pre, course, state)) {
                return true;
            }
        }
        state[i] = 2;
        return false;
    }
}