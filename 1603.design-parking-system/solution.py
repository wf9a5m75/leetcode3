class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.capacities = [big, medium, small]
        self.status = [0, 0, 0]

    def addCar(self, carType: int) -> bool:
        self.status[carType - 1] += 1
        return (self.status[carType - 1] <= self.capacities[carType - 1])


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
