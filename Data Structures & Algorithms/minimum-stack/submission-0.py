class MinStack:


    def __init__(self):

        self.min_array=[]
        self.stack=[]
        
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_array or val <= self.min_array[-1]:
            self.min_array.append(val)
        

        

    def pop(self) -> None:
        v=self.stack[-1]
        if v == self.min_array[-1]:
            self.min_array.pop()

        self.stack.pop()
        
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_array[-1]
        
