class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        max_len = 0
        
        while r < len(s)+1:
            s_slice = s[l:r]
            if len(s_slice) == len(set(s_slice)):
                r+=1
                if len(s_slice) > max_len:
                    max_len = len(s_slice)
            else:
                l += 1
                
        return max_len

    
    
"""
sliding window

while r < len+1
max_len = max(max_len, len_slice)

check unique:
len(set(slice)) == len(slice)
"""
