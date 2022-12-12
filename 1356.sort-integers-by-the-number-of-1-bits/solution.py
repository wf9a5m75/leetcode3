class Solution:
    mem = {}

    def numberOfBits(self, num) -> int:
        if (num in self.mem):
            return self.mem[num]

        count = 0
        num2 = num
        while(num2 > 0):
            count += 1 if num2 & 1 == 1 else 0
            num2 >>= 1

        self.mem[num] = count
        return count

    def sortByBits(self, arr: List[int]) -> List[int]:
        result = [-1, 1000000]
        self.mem[-1] = 0
        self.mem[1000000] = 1000000

        for num in arr:
            numOfBits = self.numberOfBits(num)

            L = 0
            R = len(result) - 1
            while(L <= R):
                mid = (L + R) >> 1
                if (self.numberOfBits(result[mid]) == numOfBits):
                    if (result[mid] < num):
                        L = mid + 1
                    else:
                        R = mid - 1
                elif (self.numberOfBits(result[mid]) < numOfBits):
                    L = mid + 1
                else:
                    R = mid - 1
            result.insert(L, num)
        result.pop()
        result.pop(0)
        return result
