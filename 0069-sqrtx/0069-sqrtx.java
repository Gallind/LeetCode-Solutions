class Solution {
    public int mySqrt(int x) {
        if (x < 1) return 0;
        long i = 0;
        while (true){
            if (i * i <= x && (i + 1) * (i + 1) > x) return (int) i;
            i++;
        }
    }
}