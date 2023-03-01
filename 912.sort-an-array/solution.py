class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        q = [(0, len(nums) - 1)]

        while(q):
            start, end = q.pop(0)
            if (start >= end):
                continue
            L, R = start, end
            # pivot = nums[L]  # NG -> Timeout
            # pivot = nums[(L + R) >> 1]  # NG -> Timeout
            pivot = nums[random.randint(L, R)]  # OK

            while (L <= R):
                while(L < end) and (nums[L] < pivot):
                    L += 1
                while(start < R) and (pivot < nums[R]):
                    R -= 1
                if (L > R):
                    break
                nums[L], nums[R] = nums[R], nums[L]
                L += 1
                R -= 1

            q.append((start, R))
            q.append((L, end))
        return nums
        
