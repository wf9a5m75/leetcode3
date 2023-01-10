/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun preorderTraversal(root: TreeNode?): List<Int> {
        var curr = root
        var stack = java.util.Stack<TreeNode>()
        val results = ArrayList<Int>()
        while ((curr != null) || (!stack.isEmpty())) {
            while (curr != null) {
                results.add(curr.`val`)
                stack.add(curr)
                curr = curr.left
            }

            if (!stack.isEmpty()) {
                curr = stack.pop()
                curr = curr.right
            }
        }
        return results
    }
}
