def display(matrix):
    for row in matrix:
        print("[", end=" ")
        for elem in row:
            print("{:5}".format(elem), end=" ")
        print("]")
    print("\n") 
    
def rearrange_matrix(matrix):
    if matrix[0][0] < matrix[1][0]:
        temp = matrix[0][0]
        matrix[0][0] = matrix[1][0]
        matrix[1][0] = temp
    if matrix[0][0] < matrix[2][0]:
        temp = matrix[0][0]
        matrix[0][0] = matrix[2][0]
        matrix[2][0] = temp    
    if matrix[1][1] < matrix[2][1]:
        temp = matrix[1][1]
        matrix[1][1] = matrix[2][1]
        matrix[2][1] = temp
    return matrix
def lu_decomposition_partial(matrix):
    
    b = [row[3] for row in matrix]
    
    print ("b",b ,"\n")
    
    m21 = matrix[1][0] / matrix[0][0]
    m31 = matrix[2][0] / matrix[0][0]

    # Rule E2-(m21)E1 = E2
    for j in range(4):
        e2 = matrix[1][j]
        e1 = m21 * matrix[0][j]
        matrix[1][j] = e2 - e1

    # Rule E3-(m31)E1 = E3
    for j in range(4):
        e3 = matrix[2][j]
        e1 = m31 * matrix[0][j]
        matrix[2][j] = e3 - e1

    m32 = matrix[2][1] / matrix[1][1]

    # Rule E3-(m32)E2 = E3
    for j in range(4):
        e3 = matrix[2][j]
        e2 = m32 * matrix[1][j]
        matrix[2][j] = e3 - e2
        
        l = [
        [1, 0, 0],
        [m21, 1, 0],
        [m31, m32, 1]
        ]
        
    print("L matrix")
    display(l)

    u = [[matrix[i][j] for j in range(3)] for i in range(3)]

    print("\nU matrix")
    display(u)
    

    # Solve Lc = b
    c = [0] * 3
    c[0] = b[0] / l[0][0]
    c[1] = (b[1] - l[1][0] * c[0]) / l[1][1]
    c[2] = (b[2] - (l[2][0] * c[0] + l[2][1] * c[1])) / l[2][2]
    print("c matrix")
    print("c1 = ", c[0])
    print("c2 = ", c[1])
    print("c3 = ", c[2])
    print("\n")

    # Solve Ux = c
    x = [0] * 3
    x[2] = c[2] / u[2][2]
    x[1] = (c[1] - u[1][2] * x[2]) / u[1][1]
    x[0] = (c[0] - (u[0][1] * x[1] + u[0][2] * x[2])) / u[0][0]

    print("LU Decomposition Result")
    print("X1 = ", x[0])
    print("X2 = ", x[1])
    print("X3 = ", x[2])
    
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
result = rearrange_matrix(matrix)
print("Rearranged Matrix:")
display(result)
lu_decomposition_partial(matrix)
