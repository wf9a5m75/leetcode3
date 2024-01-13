class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counts = [0] * 26
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1
        
        # 同じ文字数＆ tをsに順序関係なく変換する、という条件なので、
        # 不足文字があっても、別の文字で補足される。
        # 補足される文字数を知りたいので、 + のカウントだけを合計する。
        ans = 0
        for cnt in counts:
            ans += max(0, cnt)
        return ans
            