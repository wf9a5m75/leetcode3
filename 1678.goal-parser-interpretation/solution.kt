class Solution {
    fun interpret(command: String): String {
        var result = ""
        var i = 0
        while(i < command.length) {
            if (command[i] == 'G') {
                result += "G"
                i += 1
            } else if (command[i] == '(') {
                if (command[i + 1] == ')') {
                    result += "o"
                    i += 2
                } else {
                    result += "al"
                    i += 4
                }
            }
        }
        return result
    }
}
