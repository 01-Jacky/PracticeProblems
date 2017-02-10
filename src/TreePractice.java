import java.util.*;

public class TreePractice {

    static void run_demo() {

    }

    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }


    public static List<Integer> preorderTraversal(TreeNode root) {
        // // Recursion
        // List<Integer> list = new ArrayList<>();
        //
        // if(root == null)
        //     return list;
        //
        // list.add(root.val);
        // list.addAll(preorderTraversal(root.left));
        // list.addAll(preorderTraversal(root.right));
        //
        // return list;

        // Iterative using a stack
        Stack<TreeNode> stack = new Stack<TreeNode>();
        List<Integer> list = new ArrayList<>();

        stack.add(root);
        while (!stack.empty())
        {
            TreeNode current = stack.pop();
            if (current != null)
            {
                list.add(current.val);
                stack.push(current.right);
                stack.push(current.left);
            }
        }

        return list;
    }

    // public List<Integer> inorderTraversal(TreeNode root) {
    //     // // Recursion
    //
    //     // Iterative using a stack
    //     Stack<TreeNode> stack = new Stack<TreeNode>();
    //     List<Integer> list = new ArrayList<>();
    //
    //
    //     stack.add(root);
    //     while (!stack.empty())
    //     {
    //         TreeNode current = stack.pop();
    //         if (current != null)
    //         {
    //             list.add(current.val);
    //             stack.push(current.right);
    //             stack.push(current.left);
    //         }
    //     }
    //
    //     return list;
    //
    //
    // }

}


