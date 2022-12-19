class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while(stack) and (temperatures[stack[-1]] < temp):
                idx = stack.pop()
                answer[idx] = i - idx

            stack.append(i)
        return answer
