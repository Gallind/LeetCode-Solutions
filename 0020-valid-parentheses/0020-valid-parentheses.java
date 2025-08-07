import java.util.ArrayDeque;
import java.util.Deque;
class Solution {
    public boolean isValid(String s) {
        int len = s.length();
        if (len == 0) return true;
        Deque<Character> pars = new ArrayDeque<>();
        for (int i = 0; i < len; i++){
            char ch = s.charAt(i);
            if (ch == '(' || ch == '[' || ch == '{'){
                pars.push(ch);
            }
            else if (pars.isEmpty()) return false;
            else if (ch == ')'){
                if (pars.pop() != '(') return false;
            }
            else if (ch == ']'){
                if (pars.pop() != '[') return false;
            }
            else if (ch == '}'){
                if (pars.pop() != '{') return false;
            }
        }
        return pars.isEmpty();
    }
}