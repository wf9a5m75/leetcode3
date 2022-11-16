class Solution {
    // you need treat n as an unsigned value
    fun hammingWeight(n:Int):Int {
        var n2 = n
        var numOfBits = 0
        while(n2 != 0) {
            n2 = n2 and (n2 - 1)
            numOfBits += 1
        }
        return numOfBits
    }
}
