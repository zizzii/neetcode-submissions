class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        m = float("infinity")
        res = []
        heap = []
        for i in range(k):
            heapq.heappush(heap,(-nums[i],i))

        m = -heap[0][0]
        res.append(m)
        for i in range(k, len(nums)):
            n = nums[i]
            last = nums[i - k]
            heapq.heappush(heap,(-nums[i], i))
            if n >= m:
                m = max(m, n)
            elif last == m:
                val, index = heapq.heappop(heap)
                while index <= i - k:
                    val, index = heapq.heappop(heap)
                m = -val
            res.append(m)


        return res