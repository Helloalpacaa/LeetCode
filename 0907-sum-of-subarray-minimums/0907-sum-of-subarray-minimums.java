class Solution {
    public int sumSubarrayMins(int[] arr) {
        int n = arr.length;
        long sumSubarrayMins = 0;
        int mod = 1000000007;
        
        Stack<Integer> stack = new Stack<>();
        int[] pse = new int[n];
        int[] nse = new int[n];
        
        // Find the Previous Smaller Element (PSE) for each element
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && arr[stack.peek()] >= arr[i]) {
                stack.pop();
            }
            pse[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(i);
        }
        
        stack.clear();
        
        // Find the Next Smaller Element (NSE) for each element
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && arr[stack.peek()] > arr[i]) {
                stack.pop();
            }
            nse[i] = stack.isEmpty() ? n : stack.peek();
            stack.push(i);
        }
        
        // Calculate the contribution of each element to the sum
        for (int i = 0; i < n; i++) {
            long leftCount = i - pse[i];
            long rightCount = nse[i] - i;
            sumSubarrayMins = (sumSubarrayMins + (leftCount * rightCount * arr[i]) % mod) % mod;
        }
        
        return (int) sumSubarrayMins;
    }
}