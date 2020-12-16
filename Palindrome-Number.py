'''
Is integer Palindrome
reverse half of the number

Time O(n)
Space O(1)
'''
class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):    # -54 < 0 or 4220 not a palindrome 
            return False
        
        b = 0
        while x > b:
            b = b * 10 + x % 10
            x //= 10
        return x == b or  x == b//10

x = 121   #true
y = -121  #false
z = 12322 #false
a = 12321 #true

sol = Solution()
print(sol.isPalindrome(x))
print(sol.isPalindrome(y))
print(sol.isPalindrome(z))
print(sol.isPalindrome(a))
