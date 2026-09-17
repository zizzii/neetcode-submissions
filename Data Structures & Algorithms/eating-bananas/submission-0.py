class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles.sort()

        minSpeed = max(piles) # valore massimo della pila
        l, r = 1, minSpeed # 1 è il minimo

        n = len(piles)
        while l <= r:
            midSpeed = (r - l)// 2 + l
            times = 0
            for p in piles:
                times += math.ceil(p / midSpeed)

            if times <= h:
                minSpeed = min(midSpeed,minSpeed)
                r = midSpeed - 1
            else:
                l = midSpeed + 1

        return minSpeed
