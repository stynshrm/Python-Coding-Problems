
class Solution:    
    def add_two(self, arr, target):
        table = {}
        result = []
        for ind, val in enumerate(arr):
            find_bal = target - val
            if table.get(find_bal) is None:
                table[val] = ind
            else:
                result = [table[find_bal], ind]
        return result
