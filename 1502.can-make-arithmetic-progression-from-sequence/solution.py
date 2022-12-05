class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        N = len(arr)
        for i in range(1, N - 1):
            if arr[i] + diff != arr[i + 1]:
                return False
        return True
