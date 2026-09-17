class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        longest = 0

        for c in charSet:
            l = cnt = 0
            for r in range(len(s)):
                if s[r] == c:
                    cnt += 1
                
                while r - l + 1 - cnt > k:
                    if s[l] == c:
                        cnt -= 1
                    l += 1
                
                longest = max(longest, r - l + 1)
        
        return longest