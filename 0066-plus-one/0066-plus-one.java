class Solution {
    public int[] plusOne(int[] digits) {
        int len = digits.length;
        int carry = 1;
        for (int i = len - 1; i >= 0; i--){
            if (carry == 0) break;
            digits[i] += carry;
            if (digits[i] >= 10){
                digits[i] = 0;
            }
            else carry = 0;
        }
        if (carry == 1){
            int[] sol = new int[len + 1];
            sol[0] = 1;
            return sol;
        }
        return digits;
    }
}