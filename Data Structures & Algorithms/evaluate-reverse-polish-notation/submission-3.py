class Solution:
    from collections import deque
    def evalRPN(self, tokens: List[str]) -> int:
        # Use a stack to push and pop as needed.

        stack = deque()
        l_op = 0
        r_op = 0

        for char in tokens:
            
            # Case for operand.
            if char in ("+", "-", "*", "/"):
                r_op = int(stack.pop())
                l_op = int(stack.pop())
                
                match char:
                    case "+":
                        stack.append(l_op + r_op)
                    case "-":
                        stack.append(l_op - r_op)
                    case "*":
                        stack.append(l_op * r_op)
                    case "/":
                        stack.append(l_op / r_op)

            # No matter what the numbers just get appended.
            else:
                stack.append(char)

        # Final result is last thing left in stack at the end.
        return int(stack[-1])

        