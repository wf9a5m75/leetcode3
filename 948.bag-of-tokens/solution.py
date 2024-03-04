class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        
        L = 0
        R = len(tokens) - 1
        score = 0
        result = 0
        while (L <= R) and (score >= 0):
            # print(f"L={L}, R={R}, score={score}, power={power}")
            if (power - tokens[L] >= 0):
                score += 1
                result = max(result, score)
                power -= tokens[L]
                L += 1
                continue
                
            if (score == 0):
                break

            score -= 1
            power += tokens[R]
            R -= 1
        # print(f"L={L}, R={R}, score={score}, power={power}")
        return result    