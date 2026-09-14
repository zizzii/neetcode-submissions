class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            j, k = i+1, len(nums) - 1
            while j < k:
                sum = nums[j] + nums[k] + a
                if sum == 0:
                    ans.append([nums[j],nums[k],a])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j+=1
                elif sum < 0:
                     j+= 1
                else:
                    k -= 1

        return ans
            
        