class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        
        def solve(idx: int, path: List[int], total: int):
            if idx == len(candidates):
                if total == target:
                    print(",".join(map(str, path)))
                    results.append(path[:])
                return
            
            solve(idx + 1, path, total)

            if total + candidates[idx] <= target:
                path.append(candidates[idx])
                solve(idx, path, total + candidates[idx])
                path.pop()
        solve(0, [], 0)
        return results
