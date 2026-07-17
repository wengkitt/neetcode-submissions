class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for index, value in enumerate(nums):
            target = 0 - value
            p1 = index + 1
            p2 = len(nums) - 1
            while p2 > p1:                            
                ans = nums[p1] + nums[p2]

                if target > ans:
                    p1+=1
                
                if target < ans:
                    p2-=1
                
                if target == ans:
                    result.add(tuple(sorted([value, nums[p1], nums[p2]])))
                    p1+=1

        return [list(triplet) for triplet in result]



        