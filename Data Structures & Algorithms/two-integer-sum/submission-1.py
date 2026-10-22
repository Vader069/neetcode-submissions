class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst=[]
        for i in range(len(nums)):
            c=nums[i]
            for j in range(len(nums)):
                if(c+nums[j]==target and i!=j):
                    lst.append(i)
                    lst.append(j)
                    return lst
        