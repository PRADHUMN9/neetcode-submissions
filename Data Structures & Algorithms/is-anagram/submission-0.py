class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        dt1={}
        dt2={}
        for i in s:
            if i not in dt1:
                dt1[i]=1
            else:
                dt1[i] += 1
        
        for i in t:
            if i not in dt2:
                dt2[i]=1
            else:
                dt2[i]=dt2[i]+1

        if len(dt1.keys()) != len(dt2.keys()):
            return False

        for i in dt1.keys():
            if i not in dt2.keys():
                return False
                
        for i in dt2.keys():
            if i not in dt1.keys():
                return False

        for i in dt2.keys():
            if dt1[i] != dt2[i]:
                return False

        return True

        