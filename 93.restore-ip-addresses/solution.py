class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def backtrack(s: str, dotCnt: int) -> List[str]:
            N = len(s)
            if (N == 0):
                if (dotCnt == 4):
                    return [""]
                else:
                    return []


            if (s[0] == "0"):
                others = backtrack(s[1:], dotCnt + 1)
                results = list(map(lambda other: f"0.{other}", others))
                return results

            results = []
            val = 0
            for i in range(min(N, 4)):
                val = val * 10 + int(s[i])
                if (val > 255):
                    break

                others = backtrack(s[i + 1:], dotCnt + 1)
                for other in others:
                    results.append(f"{val}.{other}")
            return results

        results = backtrack(s, 0)
        results = list(map(lambda x: x[:len(x) - 1], results))

        return results
