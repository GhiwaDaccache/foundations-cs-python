##############
# Assignment 4
##############

def displayMenu():
    print("Please select a number from the following:",
        "\n\t1. Singly Linked List\n",
        "\t2. Check if Palindrome\n",
        "\t3. Priority Queue\n",
        "\t4. Evaluate an Infix Expression\n",
        "\t5. Graph\n",
        "\t6. Exit"
        )

def displayLLOptions():
    print("Choose an action: \n",
          "\ta. Add Node\n",
          "\tb. Display Nodes\n",
          "\tc. Search for & Delete Node\n",
          "\td. Return to main menu\n"
         )

class Nodes:
    def __init__(self, info):
        self.info = info
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def addNode(self, value):
        node = Nodes(value)
        if self.size == 0:
            self.head = node
            self.tail = node
            self.size += 1

        else:
            self.tail.next = node
            self.tail = node
            self.size += 1
            
    def displayNodes(self):
        current = self.head
        if current == None:
          print("Empty linked list")
          return 
        else:
          while current != None:
              print(current.info, end=" -> ")
              current = current.next
          print(None)

    def deleteNode(self, value):
        if self.size != 0:
            indices = []
            current = self.head
            while current != None:
                for i in range(self.size):
                    if current.info == value:
                        indices.append(i)
                    current = current.next
                break
        else:
          print("List is empty")
         
        if len(indices) == 0:
          print("The is not in the list")
        else:
          print("The value is at:", indices)
    
    
    
    
def main():
    print("Hello and welcome!\n")
    displayMenu()
    choice = int(input())
    while choice != 6:
        if choice == 1:
            displayLLOptions()
            LL_choice = input()
            linked_list = LinkedList()
            
            while LL_choice != "d":
                
                if LL_choice == "a":
                    node = int(input("Please enter a numerical value for your node: "))
                    linked_list.addNode(node)

                elif LL_choice == "b":
                    linked_list.displayNodes()
                
                elif LL_choice == "c":
                    value = int(input("Please enter the value of the node/s you wish to delete: "))
                    linked_list.deleteNode(value)
                    
                displayLLOptions() 
                LL_choice = input()
                
            print("You're back to main menu\n")
            displayMenu()
            choice = int(input())
    print("You exited.")
            
    
main()
    
