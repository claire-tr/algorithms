/**
 * Created by YunyunChen1 on 4/19/16.
 */
import apple.laf.JRSUIUtils;

import java.util.LinkedList;
import java.util.List;
public class Binary_Tree_Level_Order_Traversal_102 {

    public class TreeNode {
             int val;
             TreeNode left;
             TreeNode right;
             TreeNode(int x) { val = x; }
         }

    public class Solution {
        public List<List<Integer>> levelOrder(TreeNode root) {
            List<List<Integer>> result = new LinkedList<List<Integer>>();
            helper(root, 0, result);
            return result;
        }

        private void helper(TreeNode root, int level, List<List<Integer>> result) {
            if(root == null) return;
            if(result.size()<=level)
                result.add(new LinkedList<Integer>());
            result.get(level).add(root.val);
            helper(root.left, level+1, result);
            helper(root.right, level+1, result);
        }
    }
}
