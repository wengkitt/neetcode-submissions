class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                v1 = stack.pop()
                v2 = stack.pop()
                answer = 0
                match token:
                    case "+":
                        answer = v2 + v1
                    case "-":
                        answer = v2 - v1
                    case "*":
                        answer = v2 * v1
                    case "/":
                        answer = int(v2 / v1)
                stack.append(answer)

        return stack[-1]