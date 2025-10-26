class WordDictionary {
    class Node {
        private char val;
        private Node[] children;
        private boolean isLast;

        public Node(char val) {
            this.val = val;
            this.children = new Node[26];
            this.isLast = false;
        }
    }

    Node root;

    public WordDictionary() {
        root = new Node('0');
    }
    
    public void addWord(String word) {
        Node curr = root;
        for (char c: word.toCharArray()) {
            if (curr.children[c - 'a'] == null) {
                curr.children[c - 'a'] = new Node(c);
            }
            curr = curr.children[c - 'a'];
        }
        curr.isLast = true;
    }
    
    public boolean search(String word) {
        return searchDFS(word, root, 0);
    }

    private boolean searchDFS(String word, Node curr, int index) {
        for (int i = index; i < word.length(); i++) {
            char c = word.charAt(i);
            if (c == '.') {
                for (Node tmp : curr.children) {
                    if (tmp != null && searchDFS(word, tmp, i + 1)) {
                        return true;
                    }
                }
                return false;
            }
            if (curr.children[c - 'a'] == null) {
                return false;
            }
            curr = curr.children[c - 'a'];
        }
        return curr.isLast;
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */