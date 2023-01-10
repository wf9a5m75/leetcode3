class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mem = {}
        stack = []
        for val2 in nums2:
            while (stack) and (stack[-1] < val2):
                mem[stack.pop()] = val2
            stack.append(val2)
            mem[val2] = -1

        result = []
        for val1 in nums1:
            result.append(mem[val1])
        return result
