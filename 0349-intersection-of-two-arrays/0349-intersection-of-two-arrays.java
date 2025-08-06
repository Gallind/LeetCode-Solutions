import java.util.ArrayList;
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        ArrayList<Integer> inter = new ArrayList<>();
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int rep = -1;
        for (int num : nums1){
            if (num == rep) continue;
            rep = num;
            int num12 = Arrays.binarySearch(nums2, num);
            if (num12 >= 0){
                inter.add(nums2[num12]);
            }
        }
        int[] output = new int[inter.size()];
        for (int i = 0; i < inter.size(); i++){
            output[i] = inter.get(i);
        }
        return output;
    }
}