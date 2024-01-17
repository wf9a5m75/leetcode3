func uniqueOccurrences(arr []int) bool {
	counts := make(map[int]int)
	for _, val := range arr {
			counts[val]++
	}
	
	occurrences := make(map[int]bool)
	for _, freq := range counts {
			appearred := occurrences[freq]
			if appearred {
					return false
			}
			
			occurrences[freq] = true
	}
	return true
}