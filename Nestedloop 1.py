def input_matrix(matrix_num):
    """Function to input a 3x3 matrix from the user."""
    print(f"Enter the elements of Matrix {matrix_num} (row by row):")
    matrix = []
    for i in range(3):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        if len(row) != 3:
            print("Each row must have exactly 3 elements. Please try again.")
            return input_matrix(matrix_num)
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    """Function to add two 3x3 matrices."""
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(3)] for i in range(3)]
    return result

def display_matrix(matrix, title):
    """Function to display a 3x3 matrix."""
    print(f"\n{title}:")
    for row in matrix:
        print(' '.join(map(str, row)))

# Main Program
print("This program will add two 3x3 matrices.")

# Input two matrices
matrix1 = input_matrix(1)
matrix2 = input_matrix(2)

# Add the matrices
result_matrix = add_matrices(matrix1, matrix2)

# Display the result
display_matrix(matrix1, "Matrix 1")
display_matrix(matrix2, "Matrix 2")
display_matrix(result_matrix, "Resulting Matrix")