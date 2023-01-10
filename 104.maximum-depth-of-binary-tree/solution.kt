import kotlin.math.*
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
class DepthTreeNode (
    val node: TreeNode,
    var depth: Int
): TreeNode(node.`val`) { }

class Solution {
    fun maxDepth(root: TreeNode?): Int {
        if (root == null) return 0

        var q = ConcurrentLinkedQueue<DepthTreeNode>()
        q.offer(DepthTreeNode(root, 1))
        var mostDepth = 1
        while (!q.isEmpty()) {
            val curr = q.poll()
            mostDepth = max(mostDepth, curr.depth)

            if (curr.node.right != null) {
                q.offer(DepthTreeNode(curr.node.right, curr.depth + 1))
            }
            if (curr.node.left != null) {
                q.offer(DepthTreeNode(curr.node.left, curr.depth + 1))
            }
        }
        return mostDepth
    }
}
