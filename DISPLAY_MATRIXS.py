# Python code to display the given matrix and access different rows and columns

def display_matrix(matrix):
    """Displays the given matrix."""
    for row in matrix:
        print(row)

def access_row(matrix, row_index):
    """Returns the given row of the matrix."""
    return print(matrix[row_index])

def access_column(matrix, column_index):
    """Returns the given column of the matrix."""
    column = []
    for row in matrix:
        column.append(row[column_index])
    return print(column)
if __name__ == '__main__':
    matrix = [[1, 2, 3,4,5],
               [6, 7, 8,9,10],
               [11, 12, 13,14,15],
               [16, 17, 18,19,20]]

    # Display the matrix
    print("mat1=")
    display_matrix(matrix)
    # Access a row of the matrix
    print("1st row=")
    row = access_row(matrix, 0)
    print("3st row=")
    row = access_row(matrix, 2)
    print("1st column=")
    # Access a column of the matrix
    column = access_column(matrix, 1)
    print("3st column=")
    column = access_column(matrix, 3)
    