class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapped = {"(" : ")", "[" : "]", "{" : "}"}

        for c in s:
            if c in mapped:
                stack.append(c)

            elif(c in mapped.values() and len(stack) > 0 and len(s) % 2 == 0):
                if c == mapped[stack[-1]]:
                    stack.pop()

            else:
                return False
        
        return len(stack) == 0 

                

