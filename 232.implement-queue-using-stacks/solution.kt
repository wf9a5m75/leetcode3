import java.util.Stack

class MyQueue() {
    val s1 = Stack<Int>()
    val s2 = Stack<Int>()
    var useS1 = true

    fun push(x: Int) {
        if (!this.useS1) {
            while (!this.s2.empty()) {
                this.s1.push(this.s2.pop())
            }
            this.useS1 = true
        }
        this.s1.push(x)
    }

    fun pop(): Int {
        if (this.useS1) {
            while (!this.s1.empty()) {
                this.s2.push(this.s1.pop())
            }
            this.useS1 = false
        }
        return this.s2.pop()
    }

    fun peek(): Int {
        if (this.useS1) {
            while (!this.s1.empty()) {
                this.s2.push(this.s1.pop())
            }
            this.useS1 = false
        }
        return this.s2[this.s2.size - 1]
    }

    fun empty(): Boolean {
        return this.s1.size + this.s2.size == 0
    }

}

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
