class Solution {
    fun maxIceCream(costs: IntArray, coins: Int): Int {
        costs.sort()
        var i = 0
        var budget = coins
        while ((i < costs.size) && (budget - costs[i] >= 0)) {
            budget -= costs[i]
            i += 1
        }
        return i
    }
}
