class Solution:
    def get_subsets(self, fullset):
        subsets = [[]]
        for i in fullset:
            for s in range(len(subsets)):
                subsets.append(subsets[s] + [i])

        return subsets
    

l = Solution()
print(l.get_subsets([1,2,3]))
