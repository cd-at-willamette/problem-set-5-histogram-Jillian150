##################################################
# Name: Jillian
# Collaborators: N/A
# Estimate of time spent (hr): 1.5 hrs
##################################################

def is_magic_square(array:list[list[int]]) -> bool:
    size = len(array)
    for row in array:
        if len(row) != size:
            return False
    
    magic_sum = sum(array[0])
    
    # Check rows
    for row in array:
        if sum(row) != magic_sum:
            return False
    
    # Check columns
    for col in range(size):
        if sum(array[row][col] for row in range(size)) != magic_sum:
            return False
    
    # Check diagonals
    if sum(array[i][i] for i in range(size)) != magic_sum:
        return False
    if sum(array[i][size - 1 - i] for i in range(size)) != magic_sum:
        return False
    
    return True

small = [[8,1,6],[3,5,7],[4,9,2]]
print(is_magic_square(small))

