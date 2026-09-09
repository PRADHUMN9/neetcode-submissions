class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op=["+","-","*","/"]
        stack=[]

        for i in tokens:
            if i  not in op:
                stack.append(int(i))
            else:
                b=stack[-1]
                stack.pop()
                a=stack[-1]
                stack.pop()
                if i =="+":
                    stack.append(a + b)
                elif i =="-":
                    stack.append(a - b)
                elif i =="*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
        return stack[-1]
        