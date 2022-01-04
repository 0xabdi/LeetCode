class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # create a stack (LIFO)
        lookup = {")":"(", "}":"{", "]":"["} # Dictionary of corresponding brackets
        
        for p in s: # for each parenthesis in the string
            if p in lookup.values(): # check if it is an opening parenthesis
                stack.append(p)      # if true, add it to to the stack
            elif stack and lookup[p] == stack[-1]: # otherwise (it is a closing bracket), check if there is a corresponding bracket
                stack.pop() #remove from the stack
            else:
                return False
        return stack == []
        