/**
 * Definition for a Node.
 * class Node(var `val`: Int) {
 *     var children: List<Node?> = listOf()
 * }
 */

class Solution {
    fun preorder(root: Node?): List<Int> {
        if (root == null) return listOf()

        var stack = mutableListOf(root)
        var results = mutableListOf<Int>()
        while (stack.size > 0) {
            val curr = stack.removeAt(stack.size - 1)
            results.add(curr.`val`)
            for (i in curr.children.size - 1 downTo 0) {
                stack.add(curr.children[i]!!)
            }
        }
        return results
    }
}
