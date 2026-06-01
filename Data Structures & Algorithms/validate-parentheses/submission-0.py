class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            print(f"char: {char}")
            # If it's a closing bracket
            if char in bracket_map:
                
                # Pop the top element if stack isn't empty, otherwise use a dummy value
                top_element = stack.pop() if stack else '#'
                print(f" top_element: {top_element}")
                
                # If the mapping doesn't match the top element, it's invalid
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)
                
        # If the stack is empty, all brackets were properly matched
        return len(stack) == 0
            