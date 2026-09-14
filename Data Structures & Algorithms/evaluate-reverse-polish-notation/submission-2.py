class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)  # Truncates toward zero
        }
        
        for token in tokens:
            if token in operators:
                # Pop the operands
                # Note: Right operand (b) is popped first, then Left (a)
                b = stack.pop()
                a = stack.pop()
                # Apply the operation and push result back
                result = operators[token](a, b)
                stack.append(result)
            else:
                # It's a number (handles negatives like "-11")
                stack.append(int(token))
                
        return stack[0]
