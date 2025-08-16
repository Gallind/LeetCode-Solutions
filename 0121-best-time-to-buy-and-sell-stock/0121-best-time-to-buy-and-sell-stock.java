class Solution {
    public int maxProfit(int[] prices) {
        //if (prices == null || prices.length == 0) return 0;
        int maxP = 0;
        int min = prices[0];
        for (int i = 0; i < prices.length; i++){
            if (prices[i] < min){
                min = prices[i];
            }
            else if (prices[i] - min > maxP) maxP = prices[i] - min;
        }
        return maxP;
    }
}