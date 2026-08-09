class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        hashset=set(nums)
        for n in nums:
            if n-1 not in hashset:
                length=0
                while (n+length) in hashset:
                    length+=1
                    longest=max(longest,length)
        return longest