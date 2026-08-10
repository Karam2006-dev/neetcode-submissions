class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            match token:
                case "+":
                    n2, n1 = stack.pop(), stack.pop()
                    stack.append(n1 + n2)
                case "-":
                    n2, n1 = stack.pop(), stack.pop()
                    stack.append(n1 - n2)
                case "*":
                    n2, n1 = stack.pop(), stack.pop()
                    stack.append(n1 * n2)
                case "/":
                    n2, n1 = stack.pop(), stack.pop()
                    # int(...) per python issue: 
                    # "Assume that division between integers always truncates toward zero."
                    stack.append(int(n1 / n2))
                case _:
                    stack.append(int(token))
        return int(stack.pop())