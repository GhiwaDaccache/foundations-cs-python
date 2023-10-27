print("Assignment 3")

user_name = input("Enter your name here: ")

def displayMenu():
    print(
        "This is the menu: \n" + "\t1. Add Matrices\n" + 
          "\t2. Check Rotation\n" + "\t3. Invert Directory\n" + 
          "\t4. Convert Matrix to Dictionary\n" + 
          "\t5. Check Palindrome\n" + 
          "\t6. Search for an Element & Merge Sort\n" + "\t7. Exit\n"
              )
# displayMenu function here, prints out all the options the user can choose from.

rows = int(input("Enter the number of rows for your matrices: "))
columns = int(input("Enter the number of columns for your matrices: "))
while rows <= 0 or columns <= 0:
    print("Please enter an admissible value (>0)")
    rows = int(input("Enter the number of rows for your matrices: "))
    columns = int(input("Enter the number of columns for your matrices: "))
# First, the user specifies the size of the matrices by inserting the number of rows and columns.
# The while loop ensures that the user enters an admissible (>0) number before proceeding. 

matrix1 = []
for row in range(rows):
    matrix1.append([])
    for column in range(columns):
        print("Enter element", column, "of matrix", row, "in main matrix 1")
        numbers = int(input())
        matrix1[row].append(numbers)

# matrix1 is the first matrix the user will input. 
# First, empty lists will be added to matrix1 based on the number of rows. 
# Since the columns decide the length of the sub matrices, the user will be asked to enter the matrices' elements row*columns times, hence the nested for loop. 
# Finally, the inputs will be added to the matrix, according to their respective row.

print()        
print("Your first matrix is:\n", matrix1)
print()

matrix2 = []
for row in range(rows):
    matrix2.append([])
    for column in range(columns):
        print("Enter element", column, "of matrix", row, "in main matrix 2")
        numbers2 = int(input())
        matrix2[row].append(numbers2)

# matrix2 is the second matrix the user will input. And we will go about it the same as matrix1. 

print()        
print("Your second matrix is:\n", matrix2)
print()  

def addMatrices(matrix_a, matrix_b):   
    matrix = []
    for row in range(rows):
        matrix.append([])
        for column in range(columns):
            matrix[row].append(matrix_a[row][column] + matrix_b[row][column])
    return matrix

# In the addMatrices function we are adding both matrices that the user added above.
# We start by creating the matrix that will store the results. 
# Then, for the same number of rows as both matrix1 and matrix2 we add empty lists. 
# We index the results matrix using row to specify which matrices we are adding, then we add to it the sum of all elements at this index in all matrices. 

print("The result of added matrices is:\n", addMatrices(matrix1, matrix2))


#### IF USER CHOOSES  2
rows2 = int(input("Enter the number of rows for your first matrix: "))
columns2 = int(input("Enter the number of columns for your first matrix: "))
while rows2 <= 0 or columns2 <= 0:
    print("Please enter an admissible value (>0)")
    rows2 = int(input("Enter the number of rows for your first matrix: "))
    columns2 = int(input("Enter the number of columns for your first matrix: "))

rows3 = int(input("Enter the number of rows for your second matrix: "))
columns3 = int(input("Enter the number of columns for your second matrix: "))    
while rows3 <= 0 or columns3 <= 0:
    print("Please enter an admissible value (>0)")
    rows3 = int(input("Enter the number of rows for your second matrix: "))
    columns3 = int(input("Enter the number of columns for your second matrix: "))

if rows2 != columns3 or columns2 != rows3:
    print("The matrices are not a rotation of each other")
else:  

    matrix3 = []
    for r in range(rows2):
        matrix3.append([])
        for col in range(columns2): 
            print("Enter element", col, "of matrix", r, "in main matrix 1")
            num = int(input())
            matrix3[r].append(num)
    
    print()        
    print("Your first matrix is:\n", matrix3)
    print()
    
    
    matrix4 = [] 
    for row in range(rows3):
        matrix4.append([])
        for column in range(columns3): 
            print("Enter element", column, "of matrix", row, "in main matrix 2")
            number = int(input())
            matrix4[row].append(number)
    print()        
    print("Your second matrix is:\n", matrix4)
    print()



