class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        prefixMax = [0] * len(height)
        prefixMax[0] = height[0]
        for i in range(1, len(height)):
            prefixMax[i] = max(prefixMax[i - 1], height[i])

        suffixMin = [0] * len(height)
        suffixMin[-1] = height[- 1]
        for i in range(len(height) - 2, -1, -1):
            suffixMin[i] = max(suffixMin[i+1], height[i])

        for i in range(len(height)):
            res += min(prefixMax[i], suffixMin[i]) - height[i]
        
        return res