from typing import List

class Car:
    def __init__(self, position: int, speed: int):
        self.position = position
        self.speed = speed


    def estimate(self, target: int) -> int:
        return (target - self.position) / self.speed


    def __lt__(self, other) -> bool:
        return self.position <= other.position


    def __repr__(self) -> str:
        return f"[p:{self.position}, s:{self.speed}]"

class Solution:
    def carFleet(self,
                    target: int,
                    position: List[int],
                    speed: List[int]) -> int:

        cars: List[Car] = []
        number_of_cars: int = len(position)
        for i in range(number_of_cars):
            cars.append(Car(position[i], speed[i]))
        cars.sort()

        estimates = list(map(lambda car : car.estimate(target), cars))

        stack: List[int] = []
        for i in range(number_of_cars - 1, - 1, - 1):
            if not stack or stack[ - 1] < estimates[i]:
                stack.append(estimates[i])

        return len(stack)