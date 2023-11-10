print("Midterm Project - Ghiwa El Daccache")
print("-----------------------------------")
print()


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
    title = input("Please enter the title of the website: ")
    web_url = input("Please enter the URL of the website: ")
    tab = {"Title": title, "URL": web_url}
    open_tabs.append(tab)
    print("New tab opened for:", title)
                    
def closeTab():
    print()
    close_index = int(input("Please enter the index of the tab you wish to close: "))
    while close_index < 0 :
        print("Ivalid index. Please input a valid number (>=0)")
        close_index = int(input("Please enter the index of the tab you wish to close: "))

# https://www.geeksforgeeks.org/python-del-to-delete-objects/
# I used the del function which I read about in the article referenced above from geeksforgeeks.com
# del my_list1[i], in this format del deletes an item at a specific index i.
    del open_tabs[close_index]
    

def switchTab():
    print()
    display_index = int(input("Please enter the index of the tab you wish to switch to: "))
    while display_index < 0 :
        print("Ivalid index. Please input a valid number (>=0)")
        display_index = int(input("Please enter the index of the tab you wish to switch to: "))
    from urllib.request import urlopen
    url = open_tabs[display_index]["URL"]
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    print(html)

# openTab()
# openTab()
# openTab()
# print()
# print(open_tabs)
# print()
# closeTab()
# print()
# print(open_tabs)
# print()
# switchTab()
            

def main():
    print("Hello and welcome!")
    displayMenu()

