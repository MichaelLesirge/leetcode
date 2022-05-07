class Solution:
    def romanToInt(self, s: str) -> int:
        """
        map dict
        go though backwards. if a numbe is smaller subtrack it
        """
        romam_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        
        total = 0
        last = 0
        
        # for i in range(len(s)-1, -1, -1):
        #     num = romam_to_int[s[i]]
        for num in s[::-1]:
            num = int(num)
            if num >= last:
                total += num
            else:
                total -= num
            last = num
        
        return total
        
