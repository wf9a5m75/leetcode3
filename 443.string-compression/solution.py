class Solution:
    def compress(self, chars: List[str]) -> int:
        consectCnt = 0
        writeIdx = 0
        readIdx = 0
        N = len(chars)

        while (readIdx < N):
            startChar = chars[readIdx]
            readIdx += 1
            consectCnt = 1
            while ((readIdx < N) and
                   (startChar == chars[readIdx])):
                readIdx += 1
                consectCnt += 1

            chars[writeIdx] = startChar
            writeIdx += 1
            if (consectCnt == 1):
                continue

            for d in str(consectCnt):
                chars[writeIdx] = d
                writeIdx += 1
        return writeIdx
