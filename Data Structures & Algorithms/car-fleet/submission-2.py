class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        temp = sorted(zip(position, speed), reverse=True)
        position, speed = map(list, zip(*temp))
        
        fleet_times = []
        fleet = 0

        for i in range(len(position)):
            pos = position[i]
            time = ((target - pos) / speed[i])
            if not fleet_times or time > fleet_times[-1]:
                fleet_times.append(time)
                fleet += 1
        
        return fleet