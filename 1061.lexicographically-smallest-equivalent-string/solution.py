class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parents = [i for i in range(26)]

        def findParent(x: int)->int:
            if (parents[x] == x):
                return x
            parents[x] = findParent(parents[x])
            return parents[x]

        parentCnt = 0
        N = len(s1)
        for i in range(N):
            c1, c2 = s1[i], s2[i]
            ord1, ord2 = ord(c1) - 97, ord(c2) - 97
            p1, p2 = findParent(ord1), findParent(ord2)

            if (p1 == p2):
                continue
            elif (p1 < p2):
                parents[p2] = p1
            else:
                parents[p1] = p2

        result = ""
        for c in baseStr:
            ordC = ord(c) - 97
            p = findParent(ordC)
            result += chr(97 + parents[ordC])

        return result
