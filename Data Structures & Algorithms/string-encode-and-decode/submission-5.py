class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for i in strs:
            res += str(len(i))+'#'+i
        #print(res)
        return res

    def decode(self, s: str) -> List[str]:
        arr=[]
        i=0
        while i < len(s):
            j=i
            while s[j]!='#':
                j+=1

            lenght= int(s[i:j])
            i=j+1

            arr.append(s[i:i+lenght])
            i+=lenght

        return arr

        


