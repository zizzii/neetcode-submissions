class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(sum, i, l):
            if sum == target:
                res.append(l.copy())
                return
            
            if sum > target or i >= len(candidates):
                return

            # try i-th
            l.append(candidates[i])
            backtrack(sum + candidates[i], i + 1, l)

            l.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(sum, i + 1, l)


        backtrack(0, 0, [])

        return res 