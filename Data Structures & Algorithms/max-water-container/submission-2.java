class Solution {
    public int maxArea(int[] heights) {
        int area = 0;
        int lp = 0, rp = heights.length-1;
        while (lp <= rp) {
            int w = rp - lp;
            int h = Math.min(heights[lp], heights[rp]);
            int curr = w * h;
            area = Math.max(area, curr);
            if(heights[lp] < heights[rp]){
                lp++;
            }else{
                rp--;
            }
        }
        return area;
    }
}
