class Solution {
    public int sumSubarrayMins(int[] arr) {
        int n = arr.length;
        int[] pse = new int[n];
        int[] nse = new int[n];
        Stack<Integer> stack = new Stack<>();
        
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && arr[i] < arr[stack.peek()]) {
                stack.pop();
            }
            pse[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(i);
        }
        
        stack.clear();
        
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && arr[i] <= arr[stack.peek()]) {
                stack.pop();
            }
            nse[i] = stack.isEmpty() ? n : stack.peek();
            stack.push(i);
        }
        
        int mod = 1000000007;
        long sumSubarrayMins = 0;  
        
        for (int i = 0; i < n; i++) {
            long sum = (long) arr[i] * (i - pse[i]) * (nse[i] - i) ;
            sumSubarrayMins = (sumSubarrayMins + sum) % mod;
        }
        
        return (int) sumSubarrayMins;
    }
}