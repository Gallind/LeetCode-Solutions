/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        return initT(nums, 0, nums.length - 1);
    }
    private TreeNode initT(int[] nums, int l, int r){
        if (l > r) return null;
        int mid = l + (r - l) / 2;
        TreeNode temp = new TreeNode(nums[mid]);
        temp.left = initT(nums, l, mid - 1);
        temp.right = initT(nums, mid + 1, r);
        return temp;
    }
}