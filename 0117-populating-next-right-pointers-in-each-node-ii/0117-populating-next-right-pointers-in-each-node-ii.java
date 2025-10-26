/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        // DFS
        // Node realRoot = root;
        // while (root != null) { 
        //     Node dummy = new Node(0); // dummy.next指向每一层的第一个node不变
        //     Node curr = dummy; // 用curr去traverse这一层的每个node
        //     while (root != null) { // 如果root == null，说明这一层的node已经traverse完
        //         if (root.left != null) {
        //             curr.next = root.left;
        //             curr = curr.next;
        //         }
        //         if (root.right != null) {
        //             curr.next = root.right;
        //             curr = curr.next;
        //         }
        //         root = root.next;
        //     }
        //     root = dummy.next; // 去下一层的第一个node
        // }
        // return realRoot;

        // BFS
        if (root == null) {
            return root;
        }
        Deque<Node> queue = new ArrayDeque<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            while (size-- > 0) {
                Node tmp = queue.poll();
                if (size >= 1) {
                    tmp.next = queue.peek();
                }
                
                if (tmp.left != null) {
                    queue.add(tmp.left);
                }
                if (tmp.right != null) {
                    queue.add(tmp.right);
                }
            }
        }
        return root;
    }
}