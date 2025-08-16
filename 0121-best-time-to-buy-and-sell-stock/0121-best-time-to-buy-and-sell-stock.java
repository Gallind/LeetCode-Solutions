class Solution {
    public int maxProfit(int[] prices) {
        int maxP = 0;
        int min = prices[0];
        for (int i = 0; i < prices.length; i++){
            int temp = prices[i];
            if (temp < min){
                min = temp;
            }
            else if (temp - min > maxP) maxP = temp - min;
        }
        return maxP;
    }
}