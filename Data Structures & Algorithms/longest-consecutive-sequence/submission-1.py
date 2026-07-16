class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if (num - 1) in nums_set:
                continue
            else:
                not_found = False
                counter=1
                while not_found != True:
                    if (num + counter) in nums_set:
                        counter+=1
                    else:
                        not_found = True
                if counter > longest:
                    longest = counter
            
        return longest