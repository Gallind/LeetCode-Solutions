class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) return "";
        String currStr = strs[0];
        int currLen = currStr.length();
        for (String str : strs){
            if (str.length() < currLen){
                currLen = str.length();
                currStr = str;
            }
        }
        for (String str : strs) {
            while (currLen > str.length() || !currStr.equals(str.substring(0, currLen))) {
                currLen--;
                if (currLen == 0) {
                    return "";
                }
                currStr = currStr.substring(0, currLen);
            }
        }

        return currStr;        
    }
}