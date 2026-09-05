class Solution:
    array_len=0
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = set()
        array_len=len(nums)
        for i in nums:
            x.add(i)

        if len(x)==array_len:
            return False
        else:
            return True

        