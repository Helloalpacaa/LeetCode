class Solution {
    public boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        // 因为没有办法根据value get到key，所以我们需要建立两个hashMap，对应两个映射关系
        Map<Character, Character> map1 = new HashMap<>(); // s - t
        Map<Character, Character> map2 = new HashMap<>(); // t - s
        
        for (int i = 0; i < s.length(); i++) {
            if (map1.containsKey(s.charAt(i)) && map1.get(s.charAt(i)) != t.charAt(i)) {
                return false;
            } else if (map2.containsKey(t.charAt(i)) && map2.get(t.charAt(i)) != s.charAt(i)) {
                return false;
            }
            map1.put(s.charAt(i), t.charAt(i));
            map2.put(t.charAt(i), s.charAt(i));
        }
        
        return true;
    }
}