class Solution:
    def isValid(self, givenString: str) -> bool:
        stack = []

        if len(givenString) <= 1:
            return False
        for s in givenString:
            if s == "(" or s == "{" or s == "[":
                stack.append(s)
            else:
                if not stack:
                    return False
                if s == "]":
                    if stack.pop() != "[":
                        return False
                if s == "}":
                    if stack.pop() != "{":
                        return False
                if s == ")":
                    if stack.pop() != "(":
                        return False

        return len(stack) == 0