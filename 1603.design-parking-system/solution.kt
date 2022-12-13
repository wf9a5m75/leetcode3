class ParkingSystem(big: Int, medium: Int, small: Int) {
    val capacities = intArrayOf(big, medium, small)

    fun addCar(carType: Int): Boolean {
        this.capacities[carType - 1] -= 1
        return this.capacities[carType - 1] >= 0
    }

}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * var obj = ParkingSystem(big, medium, small)
 * var param_1 = obj.addCar(carType)
 */
