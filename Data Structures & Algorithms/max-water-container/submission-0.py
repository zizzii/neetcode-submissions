class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0
        while(l < r):
            tmp = (r -  l)*min(heights[l], heights[r])
            area = max(area, tmp)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return area