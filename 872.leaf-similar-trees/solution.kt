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
import java.util.Stack;
class Solution {
    fun leafSimilar(root1: TreeNode?, root2: TreeNode?): Boolean {
        val result1 = this.preorder(root1)
        val result2 = this.preorder(root2)

        if (result1.size != result2.size) return false
        for (i in 0 until result1.size) {
            if (result1[i] != result2[i]) return false
        }
        return true
    }
    private fun preorder(root: TreeNode?): IntArray {
        if (root == null) {
            return arrayOf<Int>().toIntArray()
        }
        var results = ArrayList<Int>()
        val stack = Stack<TreeNode>()
        stack.push(root)
        while (!stack.empty()) {
            val node: TreeNode = stack.pop()
            if ((node.left == null) && (node.right == null)) {
                results.add(node.`val`)
            } else {
                if (node.right != null) {
                    stack.push(node.right)
                }
                if (node.left != null) {
                    stack.push(node.left)
                }
            }
        }
        return results.toIntArray()
    }
}
