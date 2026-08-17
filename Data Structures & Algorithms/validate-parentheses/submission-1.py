class Solution:
    from collections import deque
    def isValid(self, s: str) -> bool:
        # Utilize a stack. Each time we see an open character, we push. Each time we see a close, we pop.

        # In order to be valid, all opens must be followed by their corresponding close.

        stack = deque()

        for char in s:
            # Case where is opening.
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
        
            # Case where is closing. Only a couple of valid options, everything else is not.
            else:
                if len(stack) ==  0:
                    return False
                    
                if char == ")" and stack[-1] == "(":
                    stack.pop()

                elif char == "}" and stack[-1] == "{":
                    stack.pop()

                elif char == "]" and stack[-1] == "[":
                    stack.pop()

                else:
                    return False

        # Stack should be empty as all open characters must have close characters.
        return len(stack) == 0