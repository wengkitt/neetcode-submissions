class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return []

        num_dict = dict()

        for index, num in enumerate(nums):
            value = target - num
            if value in num_dict:
                return [num_dict[value],index]
            num_dict[num] = index

        return []


        