# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            
        final = []
        for _ in range(k):
            max_key = None
            for key, value in counter.items():
                if value > counter.get(max_key, -1):
                    max_key = key
            final.append(max_key)
            del counter[max_key]
            
        return final
