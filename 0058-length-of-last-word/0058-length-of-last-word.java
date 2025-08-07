class Solution {
    public int lengthOfLastWord(String s) {
        int count = 0;
        boolean stillSpace = true;
        for (int i = s.length() - 1; i >= 0; i--){
            if (stillSpace && s.charAt(i) == ' ') continue;
            stillSpace = false;
            if (s.charAt(i) == ' ') return count;
            count++;
        }
        return count;
    }
}