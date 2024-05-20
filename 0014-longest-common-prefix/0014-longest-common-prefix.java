class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0 || strs == null) {
            return "";
        }
        
        String longestCommonPrefix = strs[0];
        for (int index = 1; index < strs.length; index++) {
            int i = 0;
            while (i < longestCommonPrefix.length() && i < strs[index].length() &&
                  longestCommonPrefix.charAt(i) == strs[index].charAt(i)) {
                i++;
            }
            longestCommonPrefix = longestCommonPrefix.substring(0, i);
        }
        return longestCommonPrefix;
    }
}