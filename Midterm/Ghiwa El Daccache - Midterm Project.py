print("Midterm Project - Ghiwa El Daccache")
print("-----------------------------------")
print()

def displayMenu():
    print(
          "This is the menu. Please make a selection from the following: \n" +
          "\t1. Open Tab\n" + 
          "\t2. Close Tab\n" + "\t3. Switch Tab\n" + 
          "\t4. Display All Tabs\n" + "\t5. Open Nested Tab\n" +
          "\t6. Clear All Tabs\n" + "\t7. Save Tabs\n" +
          "\t8. Import Tabs\n" + "\t9. Exit"
          )
        
def openTab():
  print("New tab")
  input("Please enter the title of the website: ")
  input("Please enter the URL of the website: ")


openTab()  

def main():
    print("Hello and welcome!")
    displayMenu()

