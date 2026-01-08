import java.util.ArrayList;
import java.util.List;
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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> lst = new ArrayList<>();
        return inorderT(root, lst);
    }
    private List<Integer> inorderT(TreeNode root, List<Integer> lst){
        if (root == null) return lst;
        inorderT(root.left, lst);
        lst.add(root.val);
        inorderT(root.right, lst);
        return lst;
    }
}