"""
STATEMENT
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
CLARIFICATIONS
- Can there be leading zeros? No, except the number zero.
- I am confirming that the number of digits in the two numbers can be different? Yes.
EXAMPLES
(2 -> 4 -> 3), (5 -> 6 -> 4) -> 7 -> 0 -> 8
COMMENTS
- Since the numbers are given in reverse order, we only have to iterate the two linked lists and 
  accumulate the result in a new linked list.
- We should remember the carry.
- If one of the numbers end early, we should add the rest of the unfinished number added to the carry.
- O(m+n) time complexity and O(m+n) space complexity, where m and n are number of digits in the given numbers.
"""
"""

l1 -> 2 -> 4 -> 3 , reverse order so number is 342
l2 -> 4 -> 6 -> 5 , reverse order so number is 465
add 342 + 465 = 807 ; so return 
l -> 7 -> 0 -> 8
"""

# 1st type of solution is to stringify number O(n) Time and Space complexity
# 2nd Iterative solution , using pointers O(n) Time and Space complexity


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def linked_list_str(l):
    if l is None:
        return ''
    return str(l.val) + '->' + linked_list_str(l.next)

# Make first linked list.
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
print(linked_list_str(l1))


def addTwoNumbers(l1, l2):

    print('')
    print('inside function...')

    # Declare pointers for traversal. Added for clarity.
    p1 = l1
    p2 = l2
    # Declare current carry over.
    currentCarry = 0

    # Declare cur variable to help traverse and add nodes to new list.
    # Declare head variable to be the head of the list. Initialize the lnked list
    head = cur = ListNode(0)

    # Iteration condition.
    while p1 or p2 or currentCarry:

        print(p1.val, p2.val, currentCarry)

        # Determine current value and carry over.
        currentVal = currentCarry
        currentVal += 0 if p1 is None else p1.val
        currentVal += 0 if p2 is None else p2.val
        if currentVal >= 10:
            currentVal -= 10
            currentCarry = 1
        else:
            currentCarry = 0

        print(currentVal, currentCarry)

        # Add current value as it will always atleast be '1'.
        cur.next = ListNode(currentVal)
        cur = cur.next

        # Add base cases for iterating linked lists.
        if p1 is None and p2 is None:
            break
        elif p1 is None:
            p2 = p2.next
        elif p2 is None:
            p1 = p1.next
        else:
            p1 = p1.next
            p2 = p2.next

    print('exiting...')
    print('')

    # Return next node.
    return head.next