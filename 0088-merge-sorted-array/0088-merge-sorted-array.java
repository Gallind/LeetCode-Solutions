class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] temp1 = new int[m+1];
        for (int i = 0; i < m; i++){
            temp1[i] = nums1[i];
        }
        temp1[m] = Integer.MAX_VALUE;
        int l = 0, r = 0;
        for (int i = 0; i < n+m; i++){
            if (r < n){
                if (temp1[l] < nums2[r]){
                    nums1[i] = temp1[l++];
                }
                else{
                    nums1[i] = nums2[r++];
                }
            }
            else{
                nums1[i] = temp1[l++];
            }
        }
    }
}