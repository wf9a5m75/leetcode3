class Solution:
    five = 0
    ten = 0
    twenty = 0
    LEMONADE_PRICE = 5
    
    def lemonadeChange(self, bills: List[int]) -> bool:
        billWallet = defaultdict(int)
        
        for payment in bills:
            if (payment == 5):
                self.five += 1
                continue
            if (payment == 10):
                self.ten += 1
            elif (payment == 20):
                self.twenty += 1
            else:
                raise Exception(f"Unexpected bill was given: '{payment}'")
            
            changes = payment - self.LEMONADE_PRICE
            
            # pay 10 doller bills as much as possible
            changes10 = min(self.ten, int(changes / 10))
            self.ten -= changes10
            changes -= changes10 * 10
            
            # can we pay the changes by five doller bills?
            changes5 = changes / 5
            
            if (changes5 > self.five):
                return False
            
            self.five -= changes5
        return True