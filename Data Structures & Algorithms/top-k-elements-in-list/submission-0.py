class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = dict()
        for num in nums:
            if num in num_count:
                num_count[num]+=1
            else:
                num_count[num]=1
            
        sorted_keys = [k for k, v in sorted(num_count.items(), key=lambda item: item[1], reverse=True)]

        return sorted_keys[:k]

        