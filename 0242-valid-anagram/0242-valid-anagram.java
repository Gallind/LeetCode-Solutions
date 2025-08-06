class Solution {
    public boolean isAnagram(String s, String t) {
        int len1 = s.length(), len2 = t.length();
        if (len1 != len2) return false;
        HashMap<Character, Integer> count = new HashMap();
        for (int i = 0; i < len1; i++){
            char ch = s.charAt(i);
            count.put(ch, count.getOrDefault(ch,0) + 1);
        }
        for (int i = 0; i < len2; i++){
            char ch = t.charAt(i);
            if (!count.containsKey(ch) || count.get(ch) <= 0) return false;
            count.put(ch, count.get(ch) - 1);
        }
        return true;
    }
}