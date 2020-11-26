'''
Time complexity : O(N) for each def
Space complexity : O(1)
'''


class Solution:
    delimiter = "/"
    def encode(self, s):
        ecncoded = ""
        for word in s:
            length = len(word)
            encoded += str(length) + delimiter + word

        return encoded

    def decode(self, s):
        loc = 0
        decoded = []

        while loc < len(s):
            delim_pos = s.index(delimiter, loc)
            length = int(s[delim_pos -1])
            loc = delim_pos + 1

            decoded.append(s[loc: loc + length])
            loc += length

        return decoded
