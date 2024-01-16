type RandomizedSet struct {
	keys map[int]int
	values []int
	n int
}


func Constructor() RandomizedSet {
	return RandomizedSet{
			keys: make(map[int]int),
			values: make([]int, 0),
			n: 0,
	}
}


func (this *RandomizedSet) Insert(val int) bool {
	if _, containsVal := this.keys[val]; containsVal {
			return false
	}
	
	this.keys[val] = this.n
	this.values = append(this.values, val)
	this.n += 1
	return true
}


func (this *RandomizedSet) Remove(val int) bool {
	if _, containsVal := this.keys[val]; !containsVal {
			return false
	}
	
	lastVal := this.values[this.n - 1]
	valIdx := this.keys[val]
	this.keys[lastVal] = valIdx
	this.values[valIdx] = lastVal
	
	delete(this.keys, val)
	this.values = this.values[:this.n - 1]
	this.n -= 1
	return true
}


func (this *RandomizedSet) GetRandom() int {
	idx := rand.Intn(this.n)
	return this.values[idx]
}


/**
* Your RandomizedSet object will be instantiated and called as such:
* obj := Constructor();
* param_1 := obj.Insert(val);
* param_2 := obj.Remove(val);
* param_3 := obj.GetRandom();
*/