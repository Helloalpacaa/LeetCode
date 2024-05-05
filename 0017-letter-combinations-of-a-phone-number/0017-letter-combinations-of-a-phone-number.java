class Solution {
    private StringBuilder path = new StringBuilder();
    private List<String> ans = new ArrayList<>();

    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0) {
            return ans;
        }

        String[] digitsMap = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        backtracking(digits, digitsMap, 0);
        return ans;
    }

    private void backtracking(String digits, String[] digitsMap, int startIdx) {
        if (path.length() == digits.length()) {
            ans.add(path.toString());
            return;
        }

        int digit = digits.charAt(startIdx) - '0'; // get 2
        String letters = digitsMap[digit]; // get "abc"
        for (int i = 0; i < letters.length(); i++) {
            path.append(letters.charAt(i));
            backtracking(digits, digitsMap, startIdx + 1);
            path.deleteCharAt(path.length() - 1);
        }
    }
}