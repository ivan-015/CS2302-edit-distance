# Ivan Vigliante
# CS2302 TR 10:20am-11:50am
# Lab 7
# Professor Aguirre, Diego
# TA Saha Manoj
# Date of last modification: 12/06/2018
# The purpose of this program is to implement
# the edit distance using dynamic programming.


def compute_edit_distance(s1, s2):
    if s1 == s2:
        return 0

    # Create matrix
    matrix = [-1]*(len(s1)+1)  # Each row represents a character of s1
    for i in range(len(matrix)):
        matrix[i] = [-1]*(len(s2)+1) # Each column represents a character of s2

    # Populate the first row
    for i in range(len(matrix[0])):
        matrix[0][i] = i
    # Populate first column
    for i in range(len(matrix)):
        matrix[i][0] = i

    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[i])):
            # If the two characters at the current position are the same,
            # Assign the current position to the minimum value of the immediate
            # previously computed values
            if s1[i-1] == s2[j-1]:
                matrix[i][j] = min(matrix[i][j-1],matrix[i-1][j],matrix[i-1][j-1])
            # If the characters are different, assign the current position to the minimum
            # and add one
            else:
                matrix[i][j] = min(matrix[i][j-1],matrix[i-1][j],matrix[i-1][j-1]) + 1
    # Return the value in the last row, last column to get the edit distance
    return matrix[len(s1)][len(s2)]
