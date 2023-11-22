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
        # self.tail = None
        self.size = 0
        
    def addNode(self, node):
        
        if self.size == 0:
            self.head = node
            # self.tail = node
            self.size += 1
            
        elif self.size == 1:
            self.head.next = node
            self.next = None
            self.size += 1
        
        else:
            self.next = node
            node.next = None 
            
    
def main():
    print("Hello and welcome!\n")
    displayMenu()
    choice = int(input())
    while choice != 6:
        if choice == 1:
            displayLLOptions()
            LL_choice = int(input())
            return #for now
    print("You exited.")
            
    
main()
    
