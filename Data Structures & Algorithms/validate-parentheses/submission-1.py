class Solution:
    def isValid(self, s: str) -> bool:
        if(len(s)%2==1):
            return False

        stk=[]
        
        for i in s:
            if len(stk)==0:
                stk.append(i)
    
            elif ( ( i== ')'  and stk[-1]=='(' ) or (i== ']'  and stk[-1]=='[' ) or (i== '}'  and stk[-1]=='{' )):
                stk.pop()
                #pos -=1
            else:
                stk.append(i)
                #pos +=1

        return not stk
        

        