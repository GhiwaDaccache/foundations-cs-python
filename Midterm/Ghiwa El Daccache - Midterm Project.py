print("Midterm Project - Ghiwa El Daccache")
print("-----------------------------------")
print()


open_tabs = []

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
    print()
    print("New tab")
    title = input("Please enter the title of the website: ")
    url = input("Please enter the URL of the website: ")
    tab = {"Title": title, "URL": url}
    open_tabs.append(tab)
    print("New tab opened for:", title)

# If the admin chooses (2), the system should permit the user to input the index of the
# tab they wish to close. If no index is provided, the system will close the last opened
# tab.
                    
def closeTab():
    tab_index = int(input("Please enter the index of the tab you wish to close: "))
    open_tabs[0: tab_index]
    
    del open_tabs[tab_index]
        

  

def main():
    print("Hello and welcome!")
    displayMenu()

