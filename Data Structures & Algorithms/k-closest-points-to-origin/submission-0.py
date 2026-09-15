class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i,p in enumerate(points):
            heapq.heappush(heap, (p[0]**2 + p[1]**2, i))

        res = []
        while k > 0:
            dist, i = heapq.heappop(heap)
            print(dist, " ", i)
            res.append(points[i])
            k -=1

        return res