import java.util.ArrayList;
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> nums = new HashSet<>();
        Set<Integer> inter = new HashSet<>();
        for (int num : nums1){
            nums.add(num);
        }
        for (int num : nums2){
            if (nums.contains(num)){
                inter.add(num);
            }
        }
        int[] output = new int[inter.size()];
        int i = 0;
        for (int num : inter){
            output[i++] = num;
        }
        return output;
    }
}