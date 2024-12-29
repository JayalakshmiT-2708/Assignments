def get_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Enter element [{i+1}][{j+1}]: ")))
        matrix.append(row)
    return matrix
def print_matrix(matrix):
    for row in matrix:
        print(row)
def transpose_matrix(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
matrix = get_matrix()
print("Original Matrix:")
print_matrix(matrix)
print()
transposed_matrix = transpose_matrix(matrix)
print("Transposed Matrix:")
print_matrix(transposed_matrix)
