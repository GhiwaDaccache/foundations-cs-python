print("Midterm Project - Ghiwa El Daccache")
print("-----------------------------------")
print()

from urllib.request import urlopen
import json
tab = {}
open_tabs = []


def displayMenu(): # O(1), it's constant because the number of options in the menu is fixed.
# displayMenu function here, prints out all the options the user can choose from.
    print(
          "This is the menu. Please make a selection from the following: \n", 
          "\t1. Open Tab\n",  
          "\t2. Close Tab\n",  "\t3. Switch Tab\n",  
          "\t4. Display All Tabs\n",  "\t5. Open Nested Tab\n", 
          "\t6. Clear All Tabs\n", "\t7. Save Tabs\n", 
          "\t8. Import Tabs\n", "\t9. Exit"
          )
 
def checkValidInput(index): # O(N) the while loop here is growing. N being the number of times it will loop.
    print()
# This if statement handles the case where the user doesn't enter an index, it gives it a value of -1 to use later on.
# If the user doesn't return an empty input, the program enters the while loop.  
    if index == "":
        index = -1

# The while loop here, ensures that the user input is valid by checking if:
    # The input is a number
    # To check if the user input is a number, I used .isdigit(), https://www.w3schools.com/python/ref_string_isdigit.asp 
    # This method returns True if all characters of a string are digits. Checking if it's a digit is important to first verify that it's a valid input and second to cast it later on.
    # The input is a number >-1
    # The input is a number < number of open tabs.
# Once the input is valid, the loop is exited and casts the input as an integer.        
        
    else:           
        while index.isdigit() == False or int(index) < -1 or int(index) > len(open_tabs) -1:
                print("Invalid input, please enter a valid index (>=0 or < number of open tabs)") 
                index = input()
                if index == "":
                    return -1
                    
    return int(index)
       
def openTab(parent_index): # O(1) because append and print have constant time complexity. 
    print()
 
    if parent_index == None:
        tab_type = "New tab"
    else:
        tab_type = "New nested tab"
# The user is prompted to enter the title and url of the website they wish to open.
# Then a dictionary called tab, will represent each opened tab, with the title, url and parent tab if it exists.  
# Once the tab is opened (dictionary created), it is added to a list called open tabs, to keep track of all the opened tabs and their order.    
    print(tab_type)  
    title = input("Please enter the title of the website: ")
    web_url = input("Please enter the URL of the website: ")
    tab = {"Title": title, "URL": web_url, "parent tab": parent_index}
    open_tabs.append(tab)
    print(tab_type, "opened for:", title)
    

def closeTab(): # O(N) is the time complexity of del(), with N being the opened tabs. This is because deleting an item from a list requires shifting all the elements after the deleted item to fill the gap.
    print()
# First the user is prompted to enter the index of the tab they wish to close.
    close_index = input("Please enter the index of the tab you wish to close: ")
    close_index = checkValidInput(close_index)

# https://www.geeksforgeeks.org/python-del-to-delete-objects/
# I used the del function which I read about in the article referenced above from geeksforgeeks.com
# del my_list1[i], in this format del deletes an item at a specific index i.
# The if statement below, checks if the input is -1, means the user did not enter any value, so it closes the last tab opened, otherwise it closes the specified one.
    if close_index == -1:
        close_index = len(open_tabs) - 1
    del open_tabs[close_index]

def switchTab(): 
    print()
# First the user is prompted to enter the index of the tab they wish to display.
    switch_index = input("Please enter the index of the tab you wish to switch to: ")
    switch_index = checkValidInput(switch_index)
# The if statement below, checks if the input is -1, means the user did not enter any value, so it switches to the last tab opened, otherwise it switches to the specified one.     
    if switch_index == -1: 
        switch_index = len(open_tabs) -1

    url = open_tabs[switch_index]["URL"]

# The below block is to print the HTML content of the URL. 
# Reference: https://realpython.com/python-web-scraping-practical-introduction/
# First, we import a package for web scraping from Python standard library, including the urlopen() we will use.
# To open a page, we pass url as parameter to urlopen().
# We use the .read() method on the opened page, saved in variable page.
# .read() returns a sequence of bytes, decoded using .decode() to decode the bytes to a string using UTF-8.
# UTF-8 is the dominant encoding system for the World Wide Web.
  
    page = urlopen(url)
    html = page.read().decode("utf-8")
    print(html)
  
####################################################################################################################
# def displayAllTabs():
#     for tab in open_tabs:
#         if parent_tab is None:
#             print("  " * 0 + "{tab["Title"]}, ({tab["URL"]})")
#         else:
#             print("  " * 1 + "{tab["Title"]}, ({tab["URL"]})")
#
# This is an attempt to solve the 4th user choice. 
# The for loop iterates over each element in open_tabs.
# The if statement checks if parent_tab is None (so it's not a nested tab), and prints it without an indent.
# Else it will print with an indent, however it won't be in relation to(directly below) its parent tab.  
#####################################################################################################################

def saveTabs(file_path): # O(N) because dump iterates over the elements in open_tabs. N being the number of open tabs.
# https://www.geeksforgeeks.org/json-dump-in-python/
# To save a dictionary to python, we use the .dump() method, which converts the Python objects into appropriate json objects.
# First we create the file where we are going to store the json file.
# https://www.w3schools.com/python/python_file_handling.asp
# I passed first the file name as parameter, then "w" to open a file for writing, or create it if it does not exist.  
# Then the file is closed with .close()

    file_path = open("json_tabs", "w")
    json.dump(open_tabs, file_path, indent = 3)
    file_path.close()
    print("Opened tabs are saved in", file_path)

def importTabs(file): 
# https://docs.python.org/3/tutorial/errors.html
# To handle errors of a file name not found, we use the try, except.
# The try statement is executed if no error occured, and the except is skipped. 
# If an error occured while executing try, and the error match the exception in except the except clause is executed. 
        try:
            file = open(file, "r") 
            print (file.read())
            
# https://www.w3schools.com/python/python_file_open.asp
# To read a file we first open it in read mode (r passed as parameter), then we print with .read() method to print the content of the file.
        except FileNotFoundError:
            print("File not found.")

def main():
    print("Hello and welcome!")
    displayMenu()
    selection = int(input())
    
    while selection != 9 :
        
        if selection == 1 :
            openTab(None)
            print(open_tabs)
            
        elif selection == 2 :
            print(open_tabs)
            closeTab()
            print(open_tabs)
            
        elif selection == 3 :
            print(open_tabs)
            switchTab()
            
        elif selection == 4 :
            print("Check comment line 102.")
            
        elif selection == 5 :
            parent_tab_index = input("Please enter the index of the parent tab: ")
            while parent_tab_index.isdigit() == False or int(parent_tab_index) < 0 or int(parent_tab_index) > len(open_tabs) -1:
                    print("Invalid input, please enter a valid index (>=0 or < number of open tabs)") 
                    parent_tab_index = input()
            openTab(parent_tab_index)
            
        elif selection == 6 :
            print("All tabs are cleared.")
            del open_tabs[:]
            print(open_tabs)
            
        elif selection == 7 :
            file = input("Please enter the file path to save current open tabs: ")
            saveTabs(file)
        
        elif selection == 8 :
            file_name = input("Please enter file name containing tabs to load: ")
            importTabs(file_name)  
            
        else:
            print("Please choose a number from the list")
        print()
        displayMenu()
        selection = int(input())
    print("You exited")
    
main()

