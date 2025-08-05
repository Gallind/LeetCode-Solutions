import java.util.HashMap;
class Solution {
    public int romanToInt(String s) {
        int len = s.length();
        int sum = 0;
        int[] vals = new int[256];
        vals['I'] = 1; vals['V'] = 5; vals['X'] = 10; vals['L'] = 50;
        vals['C'] = 100; vals['D'] = 500; vals['M'] = 1000;
        sum = vals[s.charAt(len - 1)];
        for (int i = len - 2; i >= 0; i--){
            int curr = vals[s.charAt(i)];
            int last = vals[s.charAt(i + 1)];
            if (curr < last) sum -= curr;
            else sum += curr;
        }
        // if (len == 0) return 0;
        // if (len == 1) return vals[s.charAt(0)];
        // for (int i = 0; i < len - 1; i++){
        //     int curr = vals[s.charAt(i)];
        //     int next = vals[s.charAt(i+1)];
        //     if (curr < next){
        //         sum += next - curr;
        //         i++;
        //         if (i == len - 2) sum += vals[s.charAt(i+1)];
        //     }
        //     else{
        //         sum += curr;
        //         if (i >= len - 2) sum += next;
        //     }
        // }
        return sum;
    }
}