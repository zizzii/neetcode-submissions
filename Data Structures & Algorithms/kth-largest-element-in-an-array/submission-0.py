class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            heapq.heappush(heap, -n)

        res = heap[0]
        for i in range(k):
            res = -heapq.heappop(heap)

        return res