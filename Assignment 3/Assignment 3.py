print("Assignment 3")
user_name = input("Enter your name here: ")
print()

def displayMenu():
# displayMenu function here, prints out all the options the user can choose from.
    print(
        "This is the menu, please make a selection: \n" + "\t1. Add Matrices\n" + 
          "\t2. Check Rotation\n" + "\t3. Invert Directory\n" + 
          "\t4. Convert Matrix to Dictionary\n" + 
          "\t5. Check Palindrome\n" + 
          "\t6. Search for an Element & Merge Sort\n" + "\t7. Exit\n"
              )

#### IF USER CHOOSES  1
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
# Finally we check if the rotated version of matrix1 matches matrix2.

        else:
            print("The matrices are not a rotation of each other")


#### IF USER CHOOSES 3
def invertDictionary():
    
    dictionary = {}
    items = int(input("Enter the number of items: "))
    for i in range(items):
        key = input("Enter you key: ")
        value = input("Enter your value: ")
        dictionary[key] = value  
    print(dictionary)
# The number of items helps define how many times the user will input keys and values. 
# Then an ordinary dictionary is created using keys and values. 
    
    inverted_dictionary = {}
# A new dictionary is created to hold the inverted values and keys. 
# So far, the program will erase duplicates and replace the key with th newest one. 
# if inverted_dictionary[value]=inverted_dictionary[value-1]:  
    for key, value in dictionary.items():
        inverted_dictionary[value] = key
    print(inverted_dictionary)
    

#### IF USER CHOOSES 4
def convertMatrix():
    classroom =[]
    students_number = int(input("Please enter the number of students: "))
    for i in range(students_number):
        print()
        print("student", i)
        first_name = input("Please enter the student's first name: ")
        last_name = input("Please enter the student's last name: ")
        stud_id = i
        job = input("Please enter the student's job title: ")
        company = input("Please enter the student's company name: ")
        classroom.append([first_name, last_name, stud_id, job, company])
        
# The user inputs the number of students, then this number will then be used to know how many times to ask for user data.
# The student ID will be automatically generated to ensure no duplicate entries. 
# Then all of the inputs will be added to a list inside of an empty list, creating a matrix. 

    students_class = {}
    for i in range(students_number):
        students_class[i] = [classroom[i][0], classroom[i][1], classroom[i][3], classroom[i][4]]
        
# For each index in classroom, we add to the dictionary by specifying the key as this index (since it also doubles as the ID).
# The values are then indexed from the list, leaving out index [i][2], for it's the student ID.
    print()
    print("The students list is the following:\n", students_class)       


#### IF USER CHOOSES 5
def checkPalindrome():
    string = input("Please enter your sentence: ")
    def verifyElements(s):
        reverse = ""
        for i in range(len(s) - 1, -1, -1):
            reverse += s[i]
# The starting index will be length of the string -1, so we start at the last index. Then the stopping index is -1 because it is excluded.
# We then start adding each character going backwards (step = -1) to an empty string. And we compare to the original one. 

        if string == reverse :
            return True 
        return False
    print(verifyElements(string))

 
#### IF USER CHOOSES 6
def searchAndSort():

    list = []
    num = int(input("Please enter the number of elements in your list: "))
    for i in range(num) :
        elements = input()
        list.append(elements)
    element = input("Please enter the element to search for: ")
#  User is prompted to enter the list and the item to search for.
 
    
    def searchList(l, e):
        for i in range(len(l)):
            if l[i] == e:
                return i
        return -1
    result = searchList(element, list)


    if result == -1:
        print("The element is not in the list")
    else:
        print("The element is at index:", result)  
        
  
# We loop through all the elements of the list and compare them to our given element. 
# If they match, we return its index. 
# If not, the program returns -1. 
# This process keeps repeating until finding the element or after having looped through the whole list. 
    
    
    def sortList(l):
        for x in range(len(l) - 1):
            for y in range(x + 1, len(l)) :
                if l[x] > l[y]:
                  temp = l[x]
                  l[x] = l[y]
                  l[y] = temp
        return l
# First we loop through all elements, then outside of this element we look for one that's lower. 
# Once we find the lower element, we swap it with our original element using temp. 

    print("The sorted list: ", sortList(list))




def main():
    displayMenu()
    selection = int(input())
    while selection != 7 :
        if selection == 1 :
            addMatrices()
        elif selection == 2 :
            checkRotation()
        elif selection == 3 :
            invertDictionary()
        elif selection == 4 :
            convertMatrix()
        elif selection == 5 :
            checkPalindrome()
        elif selection == 6 :
            searchAndSort()
        else:
            print("Please choose a number from the list")
        print()
        displayMenu()
        selection = int(input())
    print("You exited")
     
    
main()


















    



