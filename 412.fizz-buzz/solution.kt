class Solution {
    fun fizzBuzz(n: Int): List<String> {
        var results: MutableList<String> = mutableListOf()
        for (i in 1 .. n) {
            if (i % 15 == 0) {
                results.add("FizzBuzz")
            } else if (i % 3 == 0) {
                results.add("Fizz")
            } else if (i % 5 == 0) {
                results.add("Buzz")
            } else {
                results.add(i.toString())
            }
        }
        return results
    }
}
