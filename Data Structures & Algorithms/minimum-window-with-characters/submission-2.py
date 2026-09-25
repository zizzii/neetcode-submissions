class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        freqS = defaultdict(int)
        freqT = defaultdict(int)
        have, need = 0, 0
        resStart,resEnd,resLen = 0,0, float("infinity")

        if len(s) < len(t):
            return ""

        for c in t:
            freqT[c] += 1

        need = len(freqT)

        for r in range(len(s)):
            c = s[r] # letter in reference
            freqS[c] += 1

            if freqT[c] == freqS[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resEnd, resStart = r, l
                    resLen = r - l + 1
                
                freqS[s[l]] -= 1
                if freqS[s[l]] < freqT[s[l]]:
                    have -= 1
                l += 1
        l, r = resStart, resEnd
        return s[l : r + 1] if resLen != float("infinity") else ""
