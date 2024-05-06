class Solution {
    private StringBuilder path;
    private List<String> ans = new ArrayList<>();
    
    public List<String> restoreIpAddresses(String s) {
        path = new StringBuilder(s);
        backtracking(path, 0, 0);
        return ans;
    }
    
    private void backtracking(StringBuilder path, int points, int startIdx) {
        if (points == 3) {
            if (isValid(path, startIdx, path.length() - 1)) {
                ans.add(path.toString());
            }
            return;
        }
        
        for (int i = startIdx; i < path.length(); i++) {
            if (!isValid(path, startIdx, i)) {
                break;
            }
            path.insert(i + 1, ".");
            backtracking(path, points + 1, i + 2);
            path.deleteCharAt(i + 1);
        }
    }
    
    private boolean isValid(StringBuilder path, int i, int j) {
        if (i >= path.length()) {
            return false;
        }
        
        if (path.charAt(i) == '0' && i < j) {
            return false;
        }
        
        if (j - i + 1 > 3) {
            return false;
        }
        
        if (Integer.parseInt(path.substring(i, j + 1)) > 255) {
            return false;
        }
        
        return true;
    }
}