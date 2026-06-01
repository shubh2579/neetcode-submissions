class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        # If minstack is empty, this first value is automatically the minimum
        if not self.minstack:
            self.minstack.append(val)
        else:
            # Look at the PREVIOUS minimum from the top of the minstack
            current_min = self.minstack[-1]
            if val < current_min:
                self.minstack.append(val)
            else:
                self.minstack.append(current_min)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        
