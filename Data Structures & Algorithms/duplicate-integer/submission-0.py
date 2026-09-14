class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        com = set(nums)
        return len(com) != len(nums)