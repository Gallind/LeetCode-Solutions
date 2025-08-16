class Solution {
    public long maximumTripletValue(int[] nums) {
        long maxT = 0, maxE = 0, diff = 0;
        for (int num : nums){
            maxT = Math.max(maxT, num * diff);
            diff = Math.max(diff, maxE - num);
            maxE = Math.max(maxE, num);
        }
        return maxT;
    }
}