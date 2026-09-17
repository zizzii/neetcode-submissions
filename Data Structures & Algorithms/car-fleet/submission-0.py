class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] # time

        pairs = [(pos,speed) for (pos,speed) in zip(position, speed)]

        pairs.sort(key=lambda x:x[0], reverse=True)

        for pos, speed in pairs:
            time = (target - pos) / speed
            if len(stack) == 0:
                heapq.heappush(stack, time)
            elif time > stack[-1]:
                heapq.heappush(stack,time)

        return len(stack)