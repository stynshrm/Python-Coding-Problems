'''
	Given a string, find the length of the longest substring without repeating characters.
	Examples:
	Given "abcabcbb", the answer is "abc", which the length is 3.
	Given "bbbbb", the answer is "b", with the length of 1.
	Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
# space O(1)

def longestUniqueSubsttr(string):        
   # Creating a set to store the last positions of occurrence 
    seen = {} 
    maximum_length = 0
   
    # starting the inital point of window to index 0 
    start = 0 
       
    for end in range(len(string)): 

        # Checking if we have already seen the element or not 
        if string[end] in seen: 
  
            # If we have seen the number, move the start pointer 
            # to position after the last occurrence 
            start = max(start, seen[string[end]] + 1) 
   
        # Updating the last seen value of the character 
        seen[string[end]] = end 
        maximum_length = max(maximum_length, end-start + 1) 
    return maximum_length
