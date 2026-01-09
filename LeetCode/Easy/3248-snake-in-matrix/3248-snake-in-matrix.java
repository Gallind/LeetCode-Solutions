class Solution {
    public int finalPositionOfSnake(int n, List<String> commands) {
        int[] countC = new int[4];
        for (String str: commands){
            if (str.equals("UP")) countC[0]++;
            else if (str.equals("DOWN")) countC[1]++;
            else if (str.equals("RIGHT")) countC[2]++;
            else if (str.equals("LEFT")) countC[3]++;
        }
        int down = countC[1] - countC[0];
        int right = countC[2] - countC[3];
        return down * n + right;
    }
}