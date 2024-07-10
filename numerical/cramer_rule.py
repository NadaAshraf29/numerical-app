
def display(matrix):
    for row in matrix:
        print("[", end=" ")
        for elem in row:
            print("{:5}".format(elem), end=" ")
        print("]")
    print("\n") 
    
def copy_matrix(matrix, copy):

    for i in range(3):
        for j in range(3):
            copy[i][j] = matrix[i][j]

copy = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def cramer_rule(matrix):
    deta = [0] * 3
    x=[0]*3
    b = [row[3] for row in matrix]
    print ("b",b ,"\n")
    r0 = matrix[0][0] * ((matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1]))
    r1 = matrix[0][1] * ((matrix[1][0] * matrix[2][2]) - (matrix[1][2] * matrix[2][0]))
    r2 = matrix[0][2] * ((matrix[1][0] * matrix[2][1]) - (matrix[1][1] * matrix[2][0]))
    detAo = r0 - (r1) + r2
    print("delta a =",detAo)

    for i in range(3):
        copy_matrix(matrix, copy)
        
    
        copy[0][i] = matrix[0][3]
        copy[1][i] = matrix[1][3]
        copy[2][i] = matrix[2][3]
            
        r0 = copy[0][0] * ((copy[1][1] * copy[2][2]) - (copy[1][2] * copy[2][1]))
        r1 = copy[0][1] * ((copy[1][0] * copy[2][2]) - (copy[1][2] * copy[2][0]))
        r2 = copy[0][2] * ((copy[1][0] * copy[2][1]) - (copy[1][1] * copy[2][0]))
        deta [i]= r0 - (r1) + r2
        print("A[" ,(i + 1) ,"] = " ,deta[i] ,"\n")
        
    for i in range(3):
        x[i]=deta[i] / detAo    
        print( "x", i+1 , x[i])

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
cramer_rule(matrix)   
