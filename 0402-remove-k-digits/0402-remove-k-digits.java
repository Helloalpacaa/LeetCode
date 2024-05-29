class Solution {
    public String removeKdigits(String num, int k) {
        if (num.length() <= k) {
            return "0";
        }
        
        StringBuilder sb = new StringBuilder();
        int n = num.length();
        
        for (char c: num.toCharArray()) {
            while (sb.length() != 0 && k > 0 && c < sb.charAt(sb.length() - 1)) {
                sb.deleteCharAt(sb.length() - 1);
                k--;
            }
            sb.append(c);
        }
        
        while (k > 0) {
            sb.deleteCharAt(sb.length() - 1);
            k--;
        }
        
        while (sb.length() > 1 && sb.charAt(0) == '0') {
            sb.deleteCharAt(0);
        }
        
        return sb.toString();
    }
}