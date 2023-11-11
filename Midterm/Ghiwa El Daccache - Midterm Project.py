print("Midterm Project - Ghiwa El Daccache")
print("-----------------------------------")
print()

from urllib.request import urlopen
tab = {}
open_tabs = []

def displayMenu():
# displayMenu function here, prints out all the options the user can choose from.
    print(
          "This is the menu. Please make a selection from the following: \n" +
          "\t1. Open Tab\n" + 
          "\t2. Close Tab\n" + "\t3. Switch Tab\n" + 
          "\t4. Display All Tabs\n" + "\t5. Open Nested Tab\n" +
          "\t6. Clear All Tabs\n" + "\t7. Save Tabs\n" +
          "\t8. Import Tabs\n" + "\t9. Exit"
          )
        
def openTab(parent_index):
    print()
    print("New tab")

# This if condition checks if the opened tab is a nested or a parent tab. 
# When the user chooses 1, the function will be called with none passed as parameter.
# When the user chooses 5, the user will be prompted to enter the index of the parent tab then it will be passed to the openTab() function. 
    if parent_index == None:
        title = input("Please enter the title of the website: ")
        web_url = input("Please enter the URL of the website: ")
        tab = {"Title": title, "URL": web_url}
        open_tabs.append(tab)
        print("New tab opened for:", title)
        
    else:
        title = input("Please enter the title of the website: ")
        web_url = input("Please enter the URL of the website: ")
# The user is prompted to enter the title and url of the website they wish to open.
# Then a dictionary called tab, will represent each opened tab, with th title as key, and url as value.
        tab = {"Title": title, "URL": web_url, "parent tab": parent_index}
# Once the tab is opened (dictionary created), it is added to a list called open tabs, to keep track of all the opened tabs and their order.
        open_tabs.append(tab)
        print("New nested tab opened for:", title)

def checkValidInput(index):
    if index == "":
        index = -1
    else:
        while index.isdigit() == False or int(index) < -1 or int(index) > len (open_tabs) -1:
            print("Invalid input, please enter a valid index (>=0 or < number of open tabs)") 
            checkValidInput()
            
def closeTab():
    print()
# First the user is prompted to enter the index of the tab they wish to close.
    close_index = input("Please enter the index of the tab you wish to close: ")

# This if statement handles the case where the user doesn't enter an index, it gives it a value of -1 to use later on.
# If the user doesn't return an empty input, the program enters the while loop. 
    if close_index == "":
        close_index = -1
        
# The while loop here, ensures that the user input is valid by checking if:
    # The input is a number
    # To check if the user input is a number, I used .isdigit(), https://www.w3schools.com/python/ref_string_isdigit.asp 
    # This method returns True if all characters of a string are digits. Checking if it's a digit is important to first verify that it's a valid input and second to cast it later on.
    # The input is a number <-1
    # The input is a number < number of open tabs (or len(open_tabs) -1)
# Once the input is valid, the loop is exited and casts the input as an integer.
    else:           
        while close_index.isdigit() == False or int(close_index) < -1 or int(close_index) > len(open_tabs) -1: 
           print("Invalid input, please enter a valid index (>=0 or < number of open tabs)") 
           close_index = input("Please enter the index of the tab you wish to close: ")
        close_index = int(close_index)

# https://www.geeksforgeeks.org/python-del-to-delete-objects/
# I used the del function which I read about in the article referenced above from geeksforgeeks.com
# del my_list1[i], in this format del deletes an item at a specific index i.
# The if statement below, checks if the input is -1, means the user did not enter any value, so it closes the last tab opened, otherwise it closes the specified one.
    if close_index == -1:
        del open_tabs[len(open_tabs) - 1]
    else:
        del open_tabs[close_index]

def switchTab():
    print()
# First the user is prompted to enter the index of the tab they wish to display.
    display_index = input("Please enter the index of the tab you wish to switch to: ")

# This if statement handles the case where the user doesn't enter an index, it gives it a value of -1 to use later on.
# If the user doesn't return an empty input, the program enters the while loop.  
    if display_index == "":
        display_index = -1
        
# The while loop here, ensures that the user input is valid by checking if:
    # The input is a number
    # The input is a number <-1
    # The input is a number < number of open tabs (or len(open_tabs) -1)
# Once the input is valid, the loop is exited and casts the input as an integer.
    else:           
        while display_index.isdigit() == False or int(display_index) < -1 or int(display_index) > len(open_tabs): 
           print("Invalid input, please enter a valid index (>=0 or < number of open tabs)") 
           display_index = input("Please enter the index of the tab you wish to switch to: ")
        display_index = int(display_index)

# The if statement below, checks if the input is -1, means the user did not enter any value, so it switches to the last tab opened, otherwise it switches to the specified one.     
    if display_index == -1: 
        url = open_tabs[len(open_tabs) -1]["URL"] 
    else: 
        url = open_tabs[display_index]["URL"]

# The below block is to print the HTML content of the URL. 
# Reference: https://realpython.com/python-web-scraping-practical-introduction/
# First, we import a package for web scraping from Python standard library, including the urlopen() we will use.
# To open a page, we pass url as parameter to urlopen().
# We use the .read() method on the opened page, saved in variable Page.
# .read() returns a sequence of bytes. decoded using .decode() to decode the bytes to a string using UTF-8.
# UTF-8 is the dominant encoding system for the World Wide Web.
  
    page = urlopen(url)
    html = page.read().decode("utf-8")
    print(html)

def displayTabs():
    print()
    for tab in open_tabs:
        print(tab["Title"], "is an open tab.")

    
# the system should enable users to create nested tabs by
# specifying the index of the parent tab where they want to insert additional tabs.
# After entering the index, the system should prompt the user to input the titles and
# contents for the new tabs.

openTab()
openTab()
openTab()
print()
print(open_tabs)
print()
closeTab()
print()
print(open_tabs)
print()
switchTab()
displayTabs()
openNestedTab()
print(open_tabs)



def main():
    print("Hello and welcome!")
    displayMenu()

