class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cities = defaultdict(list)
        for fromI, toI, priceI in flights:
            cities[fromI].append([toI, priceI])
        
        INF = float('inf')
        totals = [INF] * n
        totals[src] = 0
        
        q = deque([[0, src, 0]])
        while (q):
            steps, curr, total = q.popleft()
            if ((curr == dst) or
                (steps == k + 1) or
                (total >= totals[dst])):
                continue

            for toI, priceI in cities[curr]:
                if (total + priceI >= totals[toI]):
                    continue
                totals[toI] = total + priceI
                q.append([steps + 1, toI, total + priceI])
        if (totals[dst] == INF):
            return -1
        else:
            return totals[dst]