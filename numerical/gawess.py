def display(matrix):
    for row in matrix:
        print("[", end=" ")
        for elem in row:
            print("{:5}".format(elem), end=" ")
        print("]")
    print("\n")    

def gje(matrix):
    

    m21 = matrix[1][0] / matrix[0][0]
    m31 = matrix[2][0] / matrix[0][0]

    # Rule E2-(m21)E1 = E2
    for j in range(4):
        e2 = matrix[1][j]
        e1 = m21 * matrix[0][j]
        matrix[1][j] = e2 - e1
    print("step one")
    display(matrix)

    # Rule E3-(m31)E1 = E3
    for j in range(4):
        e3 = matrix[2][j]
        e1 = m31 * matrix[0][j]
        matrix[2][j] = e3 - e1
    print("step two")
    display(matrix)
    
    m32 = matrix[2][1] / matrix[1][1]

    # Rule E3-(m32)E2 = E3
    for j in range(4):
        e3 = matrix[2][j]
        e2 = m32 * matrix[1][j]
        matrix[2][j] = e3 - e2
    print("step three")
    display(matrix)

    x3 = matrix[2][3] / matrix[2][2]
    x2 = (matrix[1][3] - (matrix[1][2] * x3)) / matrix[1][1]
    x1 = (matrix[0][3] - ((matrix[0][1] * x2) + (matrix[0][2] * x3))) / matrix[0][0]

    print("Gauss Jordan Result")
    print("X1 = ", x1)
    print("X2 = ", x2)
    print("X3 = ", x3)

# Main code
matrix = []
print("Enter matrix:")
for i in range(3):
    row = []
    for j in range(4):
        print(f"row{i}{j}: ", end="")
        row.append(float(input()))
    matrix.append(row)
print("\n")    
print("the input matrix")    
display(matrix)    
gje(matrix)    