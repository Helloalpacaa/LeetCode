class Solution {
    List<String> path = new LinkedList<>();
    List<List<String>> ans = new ArrayList<>();

    public List<List<String>> partition(String s) {
        backtracking(s, 0);
        return ans;
    }

    private void backtracking(String s, int startIdx) {
        if (startIdx >= s.length()) {
            ans.add(new ArrayList<>(path));
            return;
        }

        for (int i = startIdx; i < s.length(); i++) {
            if (!isPalindrome(s, startIdx, i)) {
                continue;
            }

            path.add(s.substring(startIdx, i + 1));
            backtracking(s, i + 1);
            path.removeLast();
        }
    }

    private boolean isPalindrome(String s, int i, int j) {
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}