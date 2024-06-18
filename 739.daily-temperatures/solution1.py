from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        number_of_days = len(temperatures)
        results = [0] * number_of_days

        # Store index of the higher days
        past_days = deque()

        for today_idx in range(number_of_days):
            today = temperatures[today_idx]

            # Update the results where
            # the past day lower temperature than today
            while ((past_days) and
                    (temperatures[past_days[-1]] < today)):
                past_day_idx = past_days.pop()
                num_of_days = today_idx - past_day_idx
                results[past_day_idx] = num_of_days

            past_days.append(today_idx)
        return results
