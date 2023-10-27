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

def addMatrices(): 
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
    
      
    matrix = []
    for row in range(rows):
        matrix.append([])
        for column in range(columns):
            matrix[row].append(matrix1[row][column] + matrix2[row][column])
    return matrix

# We start by creating the matrix that will store the results. 
# Then, for the same number of rows as both matrix1 and matrix2 we add empty lists. 
# We index the results matrix using row to specify which matrices we are adding, then we add to it the sum of all elements at this index in all matrices. 

    print("The result of the added matrices is:\n", matrix)
    
    
#### IF USER CHOOSES  2
def checkRotation():
    rows = int(input("Enter the number of rows for your first matrix: "))
    columns = int(input("Enter the number of columns for your first matrix: "))
    while rows <= 0 or columns <= 0:
        print("Please enter an admissible value (>0)")
        rows = int(input("Enter the number of rows for your first matrix: "))
        columns = int(input("Enter the number of columns for your first matrix: "))

# First, the user specifies the size of the first matrix by inserting the number of rows and columns.
# The while loop ensures that the user enters an admissible (>0) number before proceeding. 
    
    rows2 = int(input("Enter the number of rows for your second matrix: "))
    columns2 = int(input("Enter the number of columns for your second matrix: "))    
    while rows2 <= 0 or columns2 <= 0:
        print("Please enter an admissible value (>0)")
        rows2 = int(input("Enter the number of rows for your second matrix: "))
        columns2 = int(input("Enter the number of columns for your second matrix: "))

# Here the user inputs the dimensions of the second matrix. 

    if rows != columns2 or columns != rows2:
        print("The matrices are not a rotation of each other")
        
# Before moving on, the program checks if the number of rows in matrix 1 matches the number of columns in matrix 2, and that number of rows in matrix 2 matches the number of columns in matrix 1.
# Because if they aren't, it is impossible that they are a rotation of each other. 
    
    else:  
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
        for row in range(rows2):
            matrix2.append([])
            for column in range(columns2): 
                print("Enter element", column, "of matrix", row, "in main matrix 2")
                numbers2 = int(input())
                matrix2[row].append(numbers2)
# The same procedure as matrix 1, is applied for matrix2.
      
        print()        
        print("Your second matrix is:\n", matrix2)
        print()
        
        rotated_matrix = []
        for column in range(columns):
            rotated_matrix.append([])
            for row in range(rows):
                rotated_matrix[column].append(matrix1[row][column])
                
# An empty list is created to rotate matrix1.
# Now the number of rows becomes the number of columns, for the values of column, empty lists are created and added to the new matrix we created.
# Since the rows now decide the length of the sub matrices, for each row, the element at index[row][column] in matrix1 will be added to the new matrix at index[column(first loop)][row(second loop)].
  
        if rotated_matrix == matrix2:
            print("The matrices are a rotation of each other")
        else:
            print("The matrices are not a rotation of each other")

# Finally we check if the rotated version of matrix1 matches matrix2.

#### IF USER CHOOSES 3

    



