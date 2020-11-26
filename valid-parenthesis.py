'''
Use a stack to store while looping through string. And pop off the stack top if we find the 
mirror image. Mirro image is tablulated in a hash map.
Retrun TRUE If stack gtes empty, else False or invalid input

Time comlexity : O(N) as one loop through the input

Space complexity: max. O(N) as we might end up storing all character in input.
'''

class Solution:
    def isValid(self, s):
        stack = []
        pairs = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in pairs:
                stack.append(char)
            elif len(stack) == 0 or pairs[stack.pop()] != char:
                return False

        return len(stack) == 0