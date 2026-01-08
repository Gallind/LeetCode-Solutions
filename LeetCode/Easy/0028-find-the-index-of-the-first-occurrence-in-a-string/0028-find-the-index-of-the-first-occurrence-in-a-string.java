class Solution {
    public int strStr(String haystack, String needle) {
        int j = needle.length();
        int n = haystack.length();
        for (int i = 0; j <= n; i++, j++){
            if (haystack.substring(i,j).equals(needle)) return i;
        }
        return -1;
    }
}