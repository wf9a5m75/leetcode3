class Solution {
    // you need treat n as an unsigned value
    fun hammingWeight(n:Int):Int {
        var numOfBits = 0
        var mask = 1
        for (i in 0..31) {
            if ((n and mask) != 0) {
                numOfBits += 1
            }
            mask = mask shl 1
        }
        return numOfBits
    }
}
