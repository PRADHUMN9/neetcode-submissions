class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dt={}
        for i in nums:
            if i not in dt:
                dt[i]=1
            else:
                dt[i] +=1

        dt = dict(sorted(dt.items(), key= lambda x:x[1], reverse = True ))

        return list(dt.keys())[:k]
        