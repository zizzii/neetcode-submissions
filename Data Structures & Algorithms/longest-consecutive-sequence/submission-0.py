class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = {}
        for n in nums:
            if n not in hash:
                hash[n] = 1

        longest = 0
        for n in nums:
            tmp = n
            if n-1 not in hash:
                while tmp+1 in hash:
                    tmp +=1
                
                longest = max(longest, tmp - n + 1)

        return longest