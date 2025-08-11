class Solution {
    
    public int climbStairs(int n) {
        int[] mem = new int[50];
        mem[0] = 0; 
        mem[1] = 1;
        mem[2] = 2;
        mem[3] = 3;
        return climb(n , mem);
    }
    private int climb(int n, int[] mem){
        if (mem[n] > 0) return mem[n];
        mem[n - 1] = climb(n - 1, mem);
        mem[n - 2] = climb(n - 2, mem);
        return mem[n - 1] + mem[n - 2];
    }
}