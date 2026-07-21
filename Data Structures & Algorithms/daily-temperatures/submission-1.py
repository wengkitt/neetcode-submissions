class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

        for index, temperature in enumerate(temperatures):
            stack = []
            counter = 0
            for temp in temperatures[index + 1:]:
                stack.append(temp)
                if temp > temperature:
                    while len(stack) != 0:
                        stack.pop()
                        counter+=1
                    break
            result.append(counter)
        
        return result
            



        