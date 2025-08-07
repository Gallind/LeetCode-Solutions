class Solution {
    public int lengthOfLastWord(String s) {
        int last = 0, count = 0;
        if (s == "") return 0;
        for (char ch : s.toCharArray()){
            if (ch != ' '){
                count++;
                last = count;
            }
            else count = 0;
        }
        return last;
    }
}