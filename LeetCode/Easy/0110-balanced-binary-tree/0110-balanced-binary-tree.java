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
    public boolean isBalanced(TreeNode root) {
        return heightT(root) != -1;
    }
    private int heightT(TreeNode root){
        if (root == null) return 0;
        TreeNode left = root.left;
        TreeNode right = root.right;
        int leftH = heightT(left);
        int rightH = heightT(right);
        if (leftH == -1 || rightH == -1 || Math.abs(leftH - rightH) > 1) return -1;
        return Math.max(leftH, rightH) + 1;
    }
}