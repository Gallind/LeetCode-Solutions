import java.util.ArrayList;
import java.util.List;
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> output = new ArrayList();
        if (strs.length < 1) return output;
        List<String> first = new ArrayList();
        first.add(strs[0]);
        output.add(first);
        for (int i = 1; i < strs.length; i++){
            String str = strs[i];
            boolean isAnag = false;
            for (int j = 0; j < output.size(); j++){
                List<String> curr = output.get(j);
                if (isAnagram(curr.get(0),str)){
                    curr.add(str);
                    isAnag = true;
                    break;
                }
            }
            if (!isAnag){
                List<String> newL = new ArrayList();
                newL.add(str);
                output.add(newL);
            }
        }


        return output;
    }
    private boolean isAnagram(String s, String t) {
        int len1 = s.length(), len2 = t.length();
        if (len1 != len2) return false;
        HashMap<Character, Integer> count = new HashMap();
        for (int i = 0; i < len1; i++){
            char ch = s.charAt(i);
            count.put(ch, count.getOrDefault(ch,0) + 1);
        }
        for (int i = 0; i < len2; i++){
            char ch = t.charAt(i);
            if (!count.containsKey(ch) || count.get(ch) <= 0){ 
                return false;
            }
            count.put(ch, count.get(ch) - 1);
        }
        return true;
    }
}