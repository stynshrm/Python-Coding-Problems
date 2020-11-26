'''
Fibbonacci series
Time O(n) - loop through n
Space O(n) - storing ways list
'''

class Solution:
    def climb(self, n):
        ways = [0, 1, 2, 3]

        if n <= 3:
            return n

        for i in range(4, n+1):
            ways.append[i-2] + [i-1]

        return ways[-1]

'''
Space O(1)
'''
class Solution:
    def climb(self, n):

         if n == 1:
            return n

        first = 1
        sec = 2

        for i in range(3, n+1):
            third = first + sec
            first = sec
            sec = third

        return sec

