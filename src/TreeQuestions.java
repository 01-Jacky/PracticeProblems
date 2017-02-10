import java.util.*;

public class TreeQuestions {

    static void run_demo() {
        // TreeNode root = new TreeNode(1);
        // root.left = new TreeNode(2);
        // root.right = new TreeNode(3);
        // root.left.left = new TreeNode(4);
        // root.left.right = new TreeNode(5);
        // root.right.left = new TreeNode(6);
        // root.right.right = new TreeNode(7);

        // TreeNode root = new TreeNode(3);
        // root.left = new TreeNode(9);
        // root.right = new TreeNode(20);
        // root.right.left = new TreeNode(15);
        // root.right.right = new TreeNode(7);

        // Wiki tree
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(7);

        root = invertTree(root);

        System.out.println("Pre order traversal: "); // Expected: 1 2 4 5 3 6 7
        printTreePreOrder(root);
        System.out.println();

        // System.out.println("In order traversal: "); // Expected: 4 2 5 1 6 3 7
        // printTreeInOrder(root);
        // System.out.println();
        //
        // System.out.println("Post order traversal: "); // Expected: 4 5 2 6 7 3 1
        // printTreePostOrder(root);
        // System.out.println();


        // printLevelOrder(root);
    }


    // Returns a list of list that represents Level order traversal
    // https://leetcode.com/problems/binary-tree-level-order-traversal/
    static List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> list = new ArrayList<List<Integer>>();

        if(root == null) return list;

        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);


        while(!q.isEmpty()){
            int nodesAtLevel = q.size();
            List<Integer> levelList = new ArrayList<>();

            for(int i = 0; i < nodesAtLevel; i++){
                TreeNode popped = q.remove();
                levelList.add(popped.val);

                if(popped.left != null)
                    q.add(popped.left);
                if(popped.right != null)
                    q.add(popped.right);
            }
            list.add(levelList);
        }
        return list;
    }

    static void printLevelOrder(TreeNode root) {
        if(root == null) return;

        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while(!q.isEmpty()){
            TreeNode popped = q.remove();

            System.out.print(popped.val + " ");
            if(popped.left != null) {
                q.add(popped.left);
            }
            if(popped.right != null) {
                q.add(popped.right);
            }
        }
    }

    static void printTreePreOrder(TreeNode node) {
        /////////// Recursive method
        // Base case
        // if(root == null) return;
        //
        // // Process me, left, right (decompose and recursion)
        // System.out.print(root.val + " ");
        // printTreePreOrder(root.left);
        // printTreePreOrder(root.right);

        // /////////// Iterative method
        Stack<TreeNode> stack = new Stack<>();
        stack.push(node);

        while(!stack.empty()){
            TreeNode popped = stack.pop();

            System.out.print(popped.val + " ");
            if(popped.right != null)
                stack.push(popped.right);
            if(popped.left != null)
                stack.push(popped.left);
        }


        // Alt form
        // Stack<TreeNode> stack = new Stack<TreeNode>();
        // while(node != null) {
        //
        //     // Process me, remember to do right, then do left
        //     System.out.print(node.val + " ");
        //
        //     if (node.right != null)
        //         stack.push(node.right);
        //
        //     node = node.left;
        //
        //     if (node == null && !stack.isEmpty())
        //         node = stack.pop();
        // }
    }

    static void printTreeInOrder(TreeNode node) {
        /////////// Recursive method
        // if(root == null) return;        // Base Case
        //
        // // Process left, me, right (decompose and recursion)
        // printTreeInOrder(root.left);
        // System.out.print(root.val + " ");
        // printTreeInOrder(root.right);

        /////////// Iterative method
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode cur = node;

        while(cur!=null || !stack.empty()){
            // Go to the left bottom while adding to the stack
            while(cur!=null){
                stack.add(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            System.out.print(cur.val + " ");
            cur = cur.right;
        }
    }

    static void printTreePostOrder(TreeNode root) {
        /////////// Recursive method
        // Base case
        if(root == null) return;

        // Process left, right, me (decompose and recursion)
        printTreePostOrder(root.left);
        printTreePostOrder(root.right);
        System.out.print(root.val + " ");

        /////////// Iterative method
    }

    static TreeNode invertTree(TreeNode root){
        // Base case
        if(root == null)
            return null;
        if(root.left == null && root.right == null)
            return root;

        // Recursively invert
        TreeNode temp = root.left;
        root.left = invertTree(root.right);
        root.right = invertTree(temp);
        return root;
    }
}



