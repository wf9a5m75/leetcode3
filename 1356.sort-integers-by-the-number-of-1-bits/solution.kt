class Solution {
    var mem = HashMap<Int, Int>()

    fun numOfBits(num: Int): Int {
        if (this.mem.contains(num)) return this.mem[num]!!

        var num2 = num
        var count = 0
        while (num2 > 0) {
            if ((num2 and 1) == 1) count++
            num2 = num2 shr 1
        }
        this.mem[num] = count
        return count
    }

    fun sortByBits(arr: IntArray): IntArray {
        var result = ArrayList<Int>()
        result.add(-1)
        result.add(1000000)

        this.mem[-1] = 0
        this.mem[1000000] = 1000000

        for (num in arr) {
            val count = this.numOfBits(num)

            var L = 0
            var R = result.size - 1
            while (L <= R) {
                val mid = (L + R) / 2

                when {
                    this.numOfBits(result[mid]) > count -> R = mid - 1
                    this.numOfBits(result[mid]) < count -> L = mid + 1
                    else -> {
                        if (result[mid] < num) {
                            L = mid + 1
                        } else {
                            R = mid - 1
                        }
                    }

                }
            }
            result.add(L, num)
        }

        result.removeAt(0)
        result.removeAt(result.size - 1)
        return result.toIntArray()
    }
}
