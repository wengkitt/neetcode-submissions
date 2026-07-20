class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
                continue

            if c == ")" or c == "}" or c == "]":
                if len(stack) == 0:
                    return False

                pop_c = stack.pop()
                
                if c == ")" and pop_c != "(":
                    return False
                
                if c == "}" and pop_c != "{":
                    return False
                
                if c == "]" and pop_c != "[":
                    return False

        if len(stack) != 0:
            return False
        
        return True
        