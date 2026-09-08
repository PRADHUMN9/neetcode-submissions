class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        max_len_ans=1
        max_len_tmp=1
        
        if not nums:
            return 0
        nums = sorted(set(nums))
        
        for i in range(1,len(nums)):
            if (nums[i-1]+1==nums[i]):
                max_len_tmp +=1
            else:
                max_len_tmp=1

            max_len_ans=max(max_len_tmp,max_len_ans)

    

        return max_len_ans
