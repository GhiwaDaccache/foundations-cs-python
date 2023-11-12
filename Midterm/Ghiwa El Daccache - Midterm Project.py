print("Midterm Project - Ghiwa El Daccache")
print("-----------------------------------")
print()

from urllib.request import urlopen
import json
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
 
def checkValidInput(index):
    print()
# This if statement handles the case where the user doesn't enter an index, it gives it a value of -1 to use later on.
# If the user doesn't return an empty input, the program enters the while loop.  
    if index == "":
        index = -1

# The while loop here, ensures that the user input is valid by checking if:
    # The input is a number
    # To check if the user input is a number, I used .isdigit(), https://www.w3schools.com/python/ref_string_isdigit.asp 
    # This method returns True if all characters of a string are digits. Checking if it's a digit is important to first verify that it's a valid input and second to cast it later on.
    # The input is a number <-1
    # The input is a number < number of open tabs (or len(open_tabs) -1)
# Once the input is valid, the loop is exited and casts the input as an integer.        
        
    else:           
        while index.isdigit() == False or int(index) < -1 or int(index) > len(open_tabs) -1:
                print("Invalid input, please enter a valid index (>=0 or < number of open tabs)") 
                index = input()
                if index == "":
                    return -1
                    
    return int(index)
       
def openTab(parent_index):
    print()

# This if condition checks if the opened tab is a nested or a parent tab. 
# When the user chooses 1, the function will be called with none passed as parameter.
# When the user chooses 5, the user will be prompted to enter the index of the parent tab then it will be passed to the function. 
    if parent_index == None:
        print("New tab")
        title = input("Please enter the title of the website: ")
        web_url = input("Please enter the URL of the website: ")
        tab = {"Title": title, "URL": web_url}
        open_tabs.append(tab)
        print("New tab opened for:", title)
        
    else:
        print("New nested tab")
        title = input("Please enter the title of the website: ")
        web_url = input("Please enter the URL of the website: ")
        tab = {"Title": title, "URL": web_url, "parent tab": parent_index}        
        #######################################################################################################
        #What if we search for the word that's in the title and make it the parent tab title instead of index.#
        #######################################################################################################
        
        
# The user is prompted to enter the title and url of the website they wish to open.
# Then a dictionary called tab, will represent each opened tab, with the title as key, and url as value.
# Once the tab is opened (dictionary created), it is added to a list called open tabs, to keep track of all the opened tabs and their order.
        open_tabs.append(tab)
        print("New nested tab opened for:", title)

def closeTab():
    print()
# First the user is prompted to enter the index of the tab they wish to close.
    close_index = input("Please enter the index of the tab you wish to close: ")
    close_index = checkValidInput(close_index)

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
    switch_index = input("Please enter the index of the tab you wish to switch to: ")
    switch_index = checkValidInput(switch_index)
# The if statement below, checks if the input is -1, means the user did not enter any value, so it switches to the last tab opened, otherwise it switches to the specified one.     
    if switch_index == -1: 
        url = open_tabs[len(open_tabs) -1]["URL"] 
    else: 
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
def displayTabs():
    print()
    for tab in open_tabs:
        print(tab["Title"], "is an open tab.")

def displayAllTabs(tab_list, parent_tab=None, indent=0):
    for tab in tab_list:
        if (parent_tab is None and "parent_tab" not in tab) or ("parent_tab" in tab and tab["parent_tab"] == parent_tab):
            print("  " * indent + f"{tab['Title']} ({tab['URL']})")
            displayAllTabs(tab_list, parent_tab=tab, indent=1)
                 
displayAllTabs(open_tabs)
########################################################################################################################

# the system should prompt the user to provide a file path as
# a parameter to save the current state of open tabs. Each tab's information, including
# title, content, and any nested tabs, should be written to the file in JSON format.
# Conduct some research for additional insights on JSON.
def saveTabs(file_path):

    json_tabs = json.dumps(open_tabs)
    
    file_path = open("json file", "w")
    file_path.write(json_tabs)
    file_path.close()
    print("Opened tabs are saved in", file_path)

openTab(None)
openTab(None)
openTab(None)

print()
print(open_tabs)
print()

closeTab()
print()
print(open_tabs)
print()

# print()
# switchTab()
# print()


# openTab(2)
# print()
# print(open_tabs)

# print()
# displayAllTabs()


def importTabs():
    pass


def main():
    print("Hello and welcome!")
    displayMenu()
    selection = int(input())
    
    while selection != 9 :
        
        if selection == 1 :
            openTab(None)
            
        elif selection == 2 :
            closeTab()
            
        elif selection == 3 :
            switchTab()
            
        elif selection == 4 :
            displayTabs()
            
        elif selection == 5 :
            parent_tab_index = input("Please enter the index of the parent tab: ")
            while parent_tab_index.isdigit() == False or int(parent_tab_index) < 0 or int(parent_tab_index) > len(open_tabs) -1:
                    print("Invalid input, please enter a valid index (>=0 or < number of open tabs)") 
                    parent_tab_index = input()
            openTab(parent_tab_index)
            
        elif selection == 6 :
            print("All tabs are cleared.")
            del open_tabs[:]
            
        elif selection == 7 :
            file = input("Please enter the file path to save current open tabs: ")
            saveTabs(file)
        
        elif selection == 8 :
            importTabs()  
            
        else:
            print("Please choose a number from the list")
        print()
        displayMenu()
        selection = int(input())
    print("You exited")
    
main()

