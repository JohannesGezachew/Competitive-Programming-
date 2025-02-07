class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        right  = 0
        msum = 0
        res = 0
        while right < len(s) :
            msum += abs(ord(s[right]) -ord(t[right]))
            if msum > maxCost:
                msum -= abs(ord(s[left]) -ord(t[left]))
                left += 1
            
            res = max(res, right - left + 1)
            right += 1
        return res
