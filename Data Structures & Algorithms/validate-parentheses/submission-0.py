class Solution:
    def isValid(self, s: str) -> bool:
        #startwith
        stack = [] 
        mapping = { ")" : "(", "}" : "{", "]" : "[" } #to check if the closing is in order
        for ch in s:
            if ch in mapping:
                if stack and stack[-1] == mapping[ch]:
                    stack.pop()
                else:
                    return False


            else: 
                stack.append(ch)
        return True if not stack else False  