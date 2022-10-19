'''2D list - each item in a list is a list'''

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][1]) 

print('---Reading each items---')
for row in matrix:
    for column in row:
        print(column)