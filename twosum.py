from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], idx]
            num_dict[num] = idx
            
        return []