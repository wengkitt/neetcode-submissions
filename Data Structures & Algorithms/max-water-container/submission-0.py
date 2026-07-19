class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        largest_amount = 0

        while p2 > p1:
            amount = (p2-p1) * min(heights[p1], heights[p2])
            if amount > largest_amount:
                largest_amount = amount
            
            if heights[p1] <= heights[p2]:
                p1+=1
            else:
                p2-=1
 
        return largest_amount