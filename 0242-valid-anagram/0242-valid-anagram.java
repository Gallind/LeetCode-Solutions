class Solution {
    public boolean isAnagram(String s, String t) {
        int len1 = s.length(), len2 = t.length();
        if (len1 != len2) return false;
        for (int i = 0; i < len1; i++){
            char ch = s.charAt(i);
            int index = t.indexOf(ch);
            if (index == -1) return false;
            else{
                String temp = t.substring(0,index);
                t = temp + t.substring(index + 1, t.length());
            }
        }
        return true;
    }
}