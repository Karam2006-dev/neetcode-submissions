class Solution {
   public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
        for (int n : nums) counts[n]++;
        
        vector<pair<int, int>> freq;
        for (auto const& [val, freq_count] : counts) {
            freq.push_back({freq_count, val});
        }
        sort(freq.rbegin(), freq.rend());

        vector<int> ans;
        for (int i = 0; i < k; i++) {
            ans.push_back(freq[i].second);
        }
        return ans;
    }
};
