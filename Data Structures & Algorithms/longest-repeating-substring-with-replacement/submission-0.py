class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charcount = {}
        left = 0
        n = len(s)
        maxcount = 0
        longest=0
        for right in range (0, n):
            charcount[s[right]] = charcount.get(s[right],0)+1
            # max frequency of a single character until now
            maxcount = max(maxcount, charcount[s[right]])
            # check if number of characters to be updated > k (input)
            if right-left+1-maxcount > k:
                charcount[s[left]] -= 1
                left += 1
            # the total length of string after replacing 'k' characters.
            # right-left+1 is the length of string after replacing 'k' characters in current window.
            longest = max(longest, right-left+1)    
        return longest