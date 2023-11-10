print("Midterm Project - Ghiwa El Daccache")
print("-----------------------------------")
print()

from urllib.request import urlopen
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
        
def openTab():
    print()
    print("New tab")
# The user is prompted to enter the title and url of the website they wish to open.
    title = input("Please enter the title of the website: ")
    web_url = input("Please enter the URL of the website: ")
# Then a dictionary called tab, will represent each opened tab.
    tab = {"Title": title, "URL": web_url}
# Once the tab is opened (dictionary created), it is added to a list called open tabs, to keep track of all the opened tabs and their order.
    open_tabs.append(tab)
    print("New tab opened for:", title)
                    
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
# 
  
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    print(html)





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
            

def main():
    print("Hello and welcome!")
    displayMenu()

