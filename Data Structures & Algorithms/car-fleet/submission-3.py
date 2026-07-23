class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_time_pair = []
        
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            position_time_pair.append((position[i], time))
        
        position_time_pair.sort()

        number_of_fleet = 0
        while len(position_time_pair) != 0:
            current_car = position_time_pair.pop()
            number_of_fleet+=1
            while len(position_time_pair) != 0 and position_time_pair[-1][1] <= current_car[1]:
                position_time_pair.pop()
       
        return number_of_fleet  

        