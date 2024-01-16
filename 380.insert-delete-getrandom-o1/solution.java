class RandomizedSet {
    private ArrayList<Integer> values = new ArrayList<>();
    private Map<Integer, Integer> keys = new HashMap<>();
    
    public boolean insert(int val) {
        if (this.keys.containsKey(val)) {
            return false;
        }
        int n = this.values.size();
        this.keys.put(val, n);
        this.values.add(val);
        return true;
    }
    
    public boolean remove(int val) {
        if (!this.keys.containsKey(val)) {
            return false;
        }
        int idx = this.keys.get(val);
        int lastVal = this.values.get(this.values.size() - 1);
        
        this.values.set(idx, lastVal);
        this.keys.put(lastVal, idx);
        
        this.values.remove(this.values.size() - 1);
        this.keys.remove(val);
        return true;
    }
    
    public int getRandom() {
        Random rand = new Random();
        return this.values.get(rand.nextInt(this.values.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */