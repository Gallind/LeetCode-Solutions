class Solution {
    public int mySqrt(int x) {
        if (x == 0 || x == 1) return x;
        return sqrt(x, 1, x);
        
    }
    private int sqrt(int x, int l, int r){
        long mid = (long) l + (r - l) / 2;
        long pow = mid * mid;
        if (l >= r){
            if ((mid * mid) <= x) return (int) mid;
            return (int) (mid - 1);
        }
        if (pow == x) return (int) mid;
        if (pow > x) return sqrt(x, l, (int)(mid - 1));
        return sqrt(x, (int)(mid + 1), r);
    }
}