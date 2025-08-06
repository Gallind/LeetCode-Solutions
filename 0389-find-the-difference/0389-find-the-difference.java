import java.util.Arrays;
class Solution {
    public char findTheDifference(String s, String t) {
        HashMap<Character, Integer> str1 = new HashMap<>();
        for (int i = 0; i < s.length(); i++){
            str1.put(s.charAt(i),str1.getOrDefault(s.charAt(i),0)+1);
        }
        for (int i = 0; i < t.length(); i++){
            char ch = t.charAt(i);
            if (!str1.containsKey(ch)) return ch;
            int res = str1.get(ch);
            if (res <= 0) return ch;
            str1.put(ch, res - 1);
        }
        return 'c';
    }
}