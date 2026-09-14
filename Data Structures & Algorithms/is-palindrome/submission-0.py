import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        #print(s)
        n=len(s)
        for i in range(len(s)//2):
            if s[i] !=s[n-i-1]:
                return False
        
        return True
        