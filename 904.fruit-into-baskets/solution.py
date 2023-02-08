class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # The basket hashmap is used for storing the number of fruits each kind.
        basket = defaultdict(int)
        max_picked = 0
        left = 0

        # Add fruit from the right index (right) of the window.
        N = len(fruits)
        for right in range(N):
            fruit = fruits[right]
            basket[fruit] += 1

            # If the current window has more than 2 types of fruit,
            # we remove fruit from the left index (left) of the window,
            # until the window has only 2 types of fruit.
            while (len(basket.keys()) > 2):
                fruit = fruits[left]
                basket[fruit] -= 1
                if (basket[fruit] == 0):
                    del basket[fruit]
                left += 1

            #  Update the max_picked
            max_picked = max(max_picked, right - left + 1)
        return max_picked
