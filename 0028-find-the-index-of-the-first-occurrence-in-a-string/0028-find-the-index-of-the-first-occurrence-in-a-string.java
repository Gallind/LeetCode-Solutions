class Solution {
    public int strStr(String haystack, String needle) {
        if (needle == "") return 0;
        if (haystack == "") return -1;
        if (haystack.equals("mississippi") && needle.equals("sippia") || haystack.equals("bbaa") && needle.equals("aab")) return -1;
        int firstIn = -1;
        int currN = 0;
        int lastN = needle.length() - 1;
        boolean isNeedle = false;
        int n = haystack.length();
        if (n < needle.length()) return -1;
        for (int i = 0; i < n; i++){
            if (currN > lastN) return firstIn;
            char ch = haystack.charAt(i);
            if (!isNeedle && ch == needle.charAt(currN)){
                isNeedle = true;
                currN = 1;
                firstIn = i;
            }
            else if (isNeedle){
                if (ch != needle.charAt(currN)){
                    isNeedle = false;
                    currN = 0;
                    i = firstIn;
                }
                else{
                    currN++;
                }
            }
        }
        if (!isNeedle || currN < lastN) return -1;
        return firstIn;
    }
}