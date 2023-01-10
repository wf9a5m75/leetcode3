class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        # Counts up each task id
        counts = Counter(tasks)

        # Calculates the number of rounds
        result = 0
        for taskId in counts:
            cnt = counts[taskId]
            if cnt == 1:
                return -1

            # Since we must do 2 or 3 tasks each round,
            # calculates both cases, and then pick the minimum number
            div2 = int(cnt / 2) + (cnt % 2)
            div3 = int(cnt / 3) + (1 if (cnt % 3 > 0) else 0)
            result += min(div2, div3)

        return result
