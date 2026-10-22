class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx={}
        for i,n in enumerate(nums):
            idx[n]=i
        for i,n in enumerate(nums):
            temp=target-n
            if(temp in idx and i!=idx[temp]):
                return [i,idx[temp]]
        return []