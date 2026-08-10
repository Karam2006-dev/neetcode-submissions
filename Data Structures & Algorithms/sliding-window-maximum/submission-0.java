class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
    if(n==0) return new int[0];

    int[] res = new int[n-k+1];
    Deque<Integer> dq = new ArrayDeque<>();

    // first window
    for(int i=0;i<k;i++){
        while(!dq.isEmpty() && nums[dq.peekLast()]<= nums[i]){
            dq.pollLast();
        }
        dq.offerLast(i);
    }
    res[0] = nums[dq.peekFirst()];
    //Remaining windows
    for(int i=k;i<n;i++){
        // remove out of wd indices
        while (!dq.isEmpty() && dq.peekFirst() <= i - k) {
                dq.pollFirst();
            }
            // maintain desc order
          while (!dq.isEmpty() && nums[dq.peekLast()] <= nums[i]) {
                dq.pollLast();
            } 
            dq.offerLast(i);
            res[i-k+1] = nums[dq.peekFirst()]; 
    }
    return res;
    }
}
