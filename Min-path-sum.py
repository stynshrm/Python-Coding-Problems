#Problem given a triangle 
#triangle=[[ 2],
#          [ 1, 4],
#          [ 3, 19, 5],
#          [12, 10, 3, 9],
#          [ 7, 11, 8, 1, 4]] 
#
# desired_sum = 15
# path = 2, 4, 5, 3, 1

'''
Recursive Solution:
    minimum = triangle[0][0]
    sum_left = minimum + triangle[1][0]
    sum_right = minimum + triangle[1][1]
    minimum = min(sum_left, sum_right)

that was for row = 0, keep moving down and repeat  

wrap in function:
def min(triangle, i=0, j=0):
    return triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])

'''
# Time : O(2**n)
# Space : O(n)

def minPathSum(triangle, i=0, j=0):
    if i == len(triangle) - 1:
        return triangle[i][j]
    else:
        return triangle[i][j] + min(minPathSum(triangle, i+1, j), minPathSum(triangle, i+1, j+1))


# Dynamic Programing
# Time : O(n**2)
# Space : O(n**2)

def minPathSum(triangle):
    cm = [[0] * len(row) for row in triangle] #cache matrix
    i = len(cm) - 1

    while i >= 0:
        for j in range(len(cm[i])):
            if i == len(triangle) - 1:
                cm[i][j] = triangle[i][j]
            else:
                cm[i][j] = triangle[i][j] + min(cm[i+1][j], cm[i+1][j+1])
            
        i -= 1
    return cm[0][0]


# Dynamic Programing 2
# Time : O(n**2)
# Space : O(n)

def minPathSum(triangle):
  temp = [0] * len(triangle)
  cm = [0] * len(triangle)
  i = len(cm)-1
  while i >= 0:
    for j in range(len(cm)):
      if i == len(triangle)-1:
        cm[j] = triangle[i][j]
      else:
        cm[j] = triangle[i][j] + min(temp[j], temp[j+1])
    temp = cm
    cm_len = len(cm)-1
    cm = [0] * cm_len
    i -= 1
  return temp[0]