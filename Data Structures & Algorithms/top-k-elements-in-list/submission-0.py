class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for n in nums:
            cnt[n] = 1 + cnt.get(n,0)

        freq = [[] for i in range(len(nums) + 1)] 
        for n, count in cnt.items():
            freq[count].append(n)
        
        ans = []
        for i in range(len(freq) - 1,0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans