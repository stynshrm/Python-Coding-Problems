'''
Time complexity : O(N+M) N and M are input lenghts
Space complexity : O(N+M)
'''



class Solution:
    def compare(self, A, B):
        stack_A = []
        stack_B = []

        for char in stack_A:
            if char == "#":
                if stack_A:   #not empty
                    stack_A.pop()
            else:
                stack_A.append()
            
        for char in stack_B:
            if char == "#":
                if stack_B:   #not empty
                    stack_B.pop()
            else:
                stack_B.append()

        return stack_A == stack_B