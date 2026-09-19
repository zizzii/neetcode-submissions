class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(sum,i, l):
            if sum == target:
                res.append(l.copy())
                return

            if sum > target or i >= len(nums):
                return

            # use nums[i]
            l.append(nums[i])
            backtrack(sum + nums[i], i, l)

            l.pop()
            backtrack(sum, i + 1, l)
    
        backtrack(0, 0, [])

        return res