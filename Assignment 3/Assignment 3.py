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
    main_matrix = []
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    for row in range(rows):
        main_matrix.append([])
        for column in range(columns):
            numbers = int(input("Enter the elements of your matrix: "))
    print(main_matrix)
            
addMatrices()

        
        
        