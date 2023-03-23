class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if (len(connections) < n - 1):
            return -1

        belongs = {i: i for i in range(n)}

        def findGroup(x)->int:
            if (x != belongs[x]):
                belongs[x] = findGroup(belongs[x])
            return belongs[x]

        grpCnt = n - 1

        for A, B in connections:
            grpA = findGroup(A)
            grpB = findGroup(B)

            if (grpA == grpB):
                continue

            # merge two groups
            grpCnt += 1
            belongs[grpCnt] = grpCnt
            belongs[grpA] = grpCnt
            belongs[grpB] = grpCnt

        # print(belongs)
        cnt = 0
        for i in range(grpCnt + 1):
            x = findGroup(i)
            if (x == i):
                cnt += 1
        # print(cnt)
        return cnt - 1
