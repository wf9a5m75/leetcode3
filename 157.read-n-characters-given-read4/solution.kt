/**
* The read4 API is defined in the parent class Reader4.
* fun read4(buf4:CharArray): Int {}
*/

class Solution:Reader4() {
    /**
      * @param buf Destination buffer
      * @param n Number of characters to read
      * @return The number of actual characters read
      */
    override fun read(buf:CharArray, n:Int): Int {
        val readBuf = CharArray(4)
        var ptr = 0
        var rc = 0
        var readBytes = 4

        while ((readBytes == 4) && (ptr < n)) {
            rc = read4(readBuf)
            readBytes = minOf(rc, n - ptr)
            repeat(readBytes) {
                buf[ptr++] = readBuf[it]
            }

        }
        return ptr
    }
}
