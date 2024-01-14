func minSteps(s string, t string) (ans int) {
	dict := [26]int{}
	for i, char := range s {
			dict[char - 'a']++
			dict[t[i] - 'a']--
	}
	
	ans = 0
	for _, cnt := range dict {
			if cnt > 0 {
					ans += cnt
			}
	}
	return ans
}