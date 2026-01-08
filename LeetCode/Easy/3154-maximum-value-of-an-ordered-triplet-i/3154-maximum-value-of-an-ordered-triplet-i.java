class Solution {
    public long maximumTripletValue(int[] nums) {
        long maxT = 0, maxE = 0, sub = 0;
        for (int num : nums){
            maxT = Math.max(maxT, num * sub);
            sub = Math.max(sub, maxE - num);
            maxE = Math.max(maxE, num);
        }
        return maxT;
    }
}