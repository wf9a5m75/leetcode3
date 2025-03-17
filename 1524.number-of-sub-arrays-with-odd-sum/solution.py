class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        odd_count = 0

        # 空の部分配列 [] の和は 0 なので偶数
        even_count = 1 

        prefix_sum = 0
        result = 0
        n = len(arr)

        for r in range(n):
            prefix_sum += arr[r]

            if prefix_sum % 2 == 0:
                # ここまでのsub-arrayの数は "odd-subarray" と "even-subarray" の合計の数。
                # subarray[l, r] (l は 0...rまで取る) の中で、"odd-subarray"は、odd_count個ある
                # 
                # prefix[0, r]がevenなので、prefix[0, l-1]がoddにならないと、subarray(l, r)がoddにならない。
                # ということは、odd_count個だけ、subarray(1, r)がoddになる。
                # だからodd_countだけを足せば良い。
                result += odd_count
                even_count += 1
            else:
                # ここまでのsub-arrayの数は "odd-subarray" と "even-subarray" の合計の数。
                # subarray[l, r] (l は 0...rまで取る) の中で、"even-subarray"は、even_count個ある
                # 
                # prefix[0, r]がoddなので、prefix[0, l-1]がevenにならないと、subarray(l, r)がevenにならない。
                # ということは、even_count個だけ、subarray(1, r)がevenになる。
                # だからeven_countだけを足せば良い。
                result += even_count
                odd_count += 1
        
        result %= mod
        return result
