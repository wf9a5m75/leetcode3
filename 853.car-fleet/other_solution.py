from typing import List

class Solution:
    def carFleet(self,
                    target: int,
                    position: List[int],
                    speed: List[int]) -> int:

        # Combine the position and speed values,
        # then reverse sort them.
        # 
        # This denotes sort cars by position.
        cars = sorted(zip(position, speed), reverse = True)

        # Pile cars which faster than the other cars.
        stack: List[int] = []
        for position, speed in cars:
            estimate = (target - position) / speed
            if not stack or stack[ - 1] < estimate:
                stack.append(estimate)

        return len(stack)
