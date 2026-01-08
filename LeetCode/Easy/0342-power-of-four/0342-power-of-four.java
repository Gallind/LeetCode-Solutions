class Solution {
    public boolean isPowerOfFour(int n) {
        return n == 1 || n != 0 && n % 4 == 0 && isPowerOfFour(n / 4);
    }
}