1. class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        
        for i,val in enumerate(nums):            
            if target-val in hashmap.keys():
                return hashmap[target-val], i
            if val not in hashmap.keys():
                hashmap[val] = i
            