/**
 * Created by YunyunChen1 on 4/17/16.
 */
public class Same_Tree_100 {
    /**
     * Definition for a binary tree node.
     *  */
      public class TreeNode {
          int val;
          TreeNode left;
          TreeNode right;
          TreeNode(int x) { val = x; }
        }
        // Don't forget to compare the val of each node.
        // Think thoroughly before starting
        public boolean isSameTree(TreeNode p, TreeNode q) {
            if(p == null && q == null)
                return true;
            if(p==null || q==null)
                return false;
            boolean isSame = true;
            if(p.val != q.val) return false;
            if(p.left != null || p.right != null){
                isSame = isSameTree(p.left, q.left);
                if(!isSame) return false;
            }

            if(p.right != null || p.right != null) {
                isSame = isSameTree(p.right, q.right);
                if(!isSame) return false;
            }

            return true;
        }

}
