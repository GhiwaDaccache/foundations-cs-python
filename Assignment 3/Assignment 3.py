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
    matrix1 = []
    rows = int(input("Enter the number of rows for your matrices: "))
    columns = int(input("Enter the number of columns for your matrices: "))
    for row in range(rows):
        matrix1.append([])
        for column in range(columns):
            print("Enter element", column, "of matrix", row, "in main matrix 1")
            numbers = int(input())
            matrix1[row].append(numbers)
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
            
    print()        
    print("Your second matrix is:\n", matrix2)
    print()  
    
    matrix = []
    for row in range(rows):
        result = []
        for column in range(columns):
            result.append(matrix1[row][column] + matrix2[row][column])
        matrix.append(result)
    print(matrix)
    
    
addMatrices()

      

  
        
        