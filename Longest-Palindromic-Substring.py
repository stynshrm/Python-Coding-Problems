class Solution:
    def longestPalindrome(self, s):
        def longestAtIndex(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            return (r - l + 1, l, r)
        
        longest = 0
        left = 0
        right = -1
        for i in range(len(s)):
            for j in range(2):
                length, l, r = longestAtIndex(s, i, i + j)
                if length > longest:
                    longest = length
                    left = l
                    right = r
        return s[left:right + 1]

x = "babad"
y = "cbbd"

sol = Solution()
print(sol.longestPalindrome(x))
print(sol.longestPalindrome(y))