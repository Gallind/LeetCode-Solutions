class Solution {
    public String longestCommonPrefix(String[] strs) {
        String output = "";
        if (strs.length == 0) return output;
        String shortest = null;
        int lenShortest = Integer.MAX_VALUE;
        for (String str : strs){
            if (str.length() < lenShortest){
                lenShortest = str.length();
                shortest = str;
            }
        }
        for (int i = 0; i < lenShortest; i++){
            char currCh = strs[0].charAt(i);
            for (String str : strs){
                if (str.charAt(i) != currCh){
                    return output;
                }
            }
            output += currCh;
        }
        return output;
    }
}