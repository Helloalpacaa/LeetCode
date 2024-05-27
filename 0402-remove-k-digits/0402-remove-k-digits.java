class Solution {
    public String removeKdigits(String num, int k) {
        if (num.length() <= k) {
            return "0";
        }
        
        // 用stringBuilder模拟stack
        StringBuilder sb = new StringBuilder();
        for (char c: num.toCharArray()) {
            while (k > 0 && sb.length() > 0 && c < sb.charAt(sb.length() - 1)) {
                sb.deleteCharAt(sb.length() - 1);
                k--;
            }
            sb.append(c);
        }
        
        // 看是否要去除掉最后一位
        while (k > 0) {
            sb.deleteCharAt(sb.length() - 1);
            k--;
        }
        
        // 去除example 2里的首字母为‘0’的情况
        while (sb.length() > 1 && sb.charAt(0) == '0') {
            sb.deleteCharAt(0);
        }
        
        return sb.toString();
    }
}