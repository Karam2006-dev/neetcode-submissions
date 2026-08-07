class Solution {
public:
    int search(vector<int>& arr, int target) {
        int st=0,end=arr.size()-1;
        while(st<=end){
            int mid=(st+end)/2;
            if(target>arr[mid]){
                st=mid+1;
            }
            else if(target<arr[mid]){
                end=mid-1;
            }
            else{
                return mid;
            }
        }
        return -1;
    }
};
