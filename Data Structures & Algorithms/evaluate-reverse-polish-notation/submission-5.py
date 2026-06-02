class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lst = []
        if len(tokens)<2:
            return int(tokens[0])
        for i in tokens:
            if i not in ['+', '-', '*', '/']:
                lst.append(i)
            else:
                b = lst.pop()
                a = lst.pop()
                
                result = int(eval(f"{a} {i} {b}"))
                lst.append(result)
        
        return int(lst[0])
    
        