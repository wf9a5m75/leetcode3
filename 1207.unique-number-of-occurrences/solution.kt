class Solution {
    fun uniqueOccurrences(arr: IntArray): Boolean {
        val counts = mutableMapOf<Int, Int>()
        
        arr.forEach { num -> 
            counts.put(num, (counts.get(num) ?: 0) + 1)
        }
        
        return counts.values.size == counts.values.toSet().size
    }
}