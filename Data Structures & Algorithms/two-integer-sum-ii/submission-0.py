class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1

        while p1 < p2:    
            diff = target - (numbers[p1]+numbers[p2])
            
            if diff<0:
                p2-=1
                continue
            
            if diff>0:
                p1+=1
                continue
            
            if diff == 0:
                return [p1+1,p2+1]

        return []


        