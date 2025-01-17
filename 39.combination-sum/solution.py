from copy import deepcopy

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = list(filter(lambda x: x <= target, candidates))
        n = len(candidates)
        results = []
        seen = set()

        def dfs(i: int, total: int, path: List[int]) -> None:
            if i == n or total > target:
                return
            if total == target:
                key = ",".join(map(str, path))
                if key in seen:
                    return
                seen.add(key)
                results.append(deepcopy(path))
                return
            
            dfs(i + 1, total, path)

            path.append(candidates[i])
            dfs(i, total + candidates[i], path)
            path.pop()
            
            if i + 1 < n:
                path.append(candidates[i + 1])
                dfs(i + 1, total + candidates[i + 1], path)
                path.pop()
        
        dfs(0, 0, [])
        return results
