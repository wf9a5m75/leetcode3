class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        N = len(piles)

        # Build a max heap-queue ... O(N) time
        hq = []
        total = 0
        for pile in piles:
            total += pile
            heapq.heappush(hq, -pile)

		# Do operations ... O(k log N) time
        for i in range(k):
            peek = heapq.heappop(hq)
            remove = int(-peek / 2)
            peek += remove
            total -= remove
            heapq.heappush(hq, peek)

        return total
