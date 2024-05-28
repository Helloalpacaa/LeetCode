class Solution {
    public int sumSubarrayMins(int[] arr) {
        int n = arr.length;
        int[] pse = new int[n]; // previous smaller element, default value is -1
        int[] nse = new int[n]; // next smaller element, default value is n
        
        Stack<Integer> stack = new Stack<>();
        
        // 栈里只存一个值或者不存值，当遇到1时，1比3小，pop 3，这时栈为空，说明1左边没有比它小的值，单调递增栈
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
        
        long sumSubarrayMins = 0;
        int mod = 1000000007;
        
        for (int i = 0; i < n; i++) {
            long contribution = (long) arr[i] * (i - pse[i]) * (nse[i] - i);
            sumSubarrayMins = (sumSubarrayMins + contribution) % mod;
        }
        
        return (int) sumSubarrayMins;
    }
}