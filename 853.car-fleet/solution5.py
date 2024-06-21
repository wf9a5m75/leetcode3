from fractions import Fraction
from typing import List

class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ahead_car = Fraction()
        fleets = 0
        for position, speed in sorted(zip(position, speed), reverse=True):
            eta = Fraction(target - position, speed)
            if ahead_car >= eta:
                continue
            ahead_car = eta
            fleets += 1
        return fleets
