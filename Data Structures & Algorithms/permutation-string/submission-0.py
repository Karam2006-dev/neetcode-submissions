class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1charcount = {}
        s2charcount = {}
        n1 = len(s1)
        n2 = len(s2)
        if n1 == 0 or n1 > n2:
            return False

        for i in range(0,n1):
            s1charcount[s1[i]] = s1charcount.get(s1[i], 0)+1
            s2charcount[s2[i]] = s2charcount.get(s2[i], 0)+1
        
        if s1charcount == s2charcount:
            return True

        for i in range(n1,n2):
            # removing the first element as i moves one step forward
            if s2charcount[s2[i-n1]] > 1:
                s2charcount[s2[i-n1]] -= 1
            else:
                del s2charcount[s2[i-n1]]
            s2charcount[s2[i]] = s2charcount.get(s2[i], 0)+1
            if s1charcount == s2charcount:
                return True
        return False