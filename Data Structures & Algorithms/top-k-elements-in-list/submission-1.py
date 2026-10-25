class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct={}
        for i in range(len(nums)):
            x=nums[i]
            if x not in dct:
                dct[x]=1
            else:
                dct[x]+=1
        newdct=sorted(dct.items(),key=lambda item: item[1])
        ans=[]
        for i in range(k):
            ans.append(newdct[len(newdct)-1-i][0])
        return ans

        