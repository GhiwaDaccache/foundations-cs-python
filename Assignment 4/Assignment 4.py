##############
# Assignment 4
##############
indices = []
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
          
          
    def searchNode(self, value):
        global indices
        indices = []
        if self.size != 0:
            index = 0
            current = self.head
            while current != None:
                if current.info == value:
                    indices.append(index)
                current = current.next
                index += 1
        
        else:
          print("List is empty")
          return False
      
        if len(indices) == 0:
          print("The value is not in the list")
          return False
        return True
    

    def deleteNode(self, index_list):
        current = self.head
        previous = self.head
        loop_index = 0
        for x in index_list:
            while loop_index != x and current.next != None:
                previous = current
                current = current.next
                loop_index += 1    
                
            if loop_index == x and current == self.head:   
                self.head = self.head.next
                current.next = None
                current = self.head
                previous = self.head
                self.size -= 1
                loop_index +=1
                
            elif loop_index == x and current.next != None:   
                previous.next = current.next
                current = current.next
                self.size -= 1
                loop_index +=1
                
            elif loop_index == x and current.next == None:
                previous.next = None
                self.tail = previous
                self.size -= 1
  
class Stack:
    def __init__(self):
        self.elements = []
        self.size = 0
    
    def push(self, value):
        self.elements.append(value)
        self.size += 1
    
    def transformList(self, string):
        for x in string:
            self.push(x)
        print(self.elements)
    
    def peek(self):
        if self.size == 0:
            print("Empty stack.")
        else:
            return self.elements[len(self.elements) - 1]
    
    def peekReverse(self):
        if self.size == 0:
            print("Empty stack.")
        else:
            return self.elements[0]
    
    def pop(self):
        if self.size == 0: 
            print("Empty stack.")
        else:
            self.elements = self.elements[:-1]
            self.size -= 1
    
    def dequeue(self): 
        if self.size == 0: 
            print("Empty stack.")
        else:
            self.elements = self.elements[1: ]
            self.size -= 1
            print(self.elements)
    
    def checkPalindrome(self):
        for i in range(len(self.elements) //2):
            while self.size > 1:
                if self.peek() == self.peekReverse():
                    self.pop()
                    self.dequeue()
                    print("The string is a palindrome")
                
                else:
                    print("The string is not a palindrome")
                    break

                           
class Student:
    def __init__(self, name, midterm_grade, final_grade, good_attitude):
# class Student, class Node and class Priority Queue
        self.name = name
        self.midterm_grade = midterm_grade
        self.final_grade = final_grade
        self.good_attitude = good_attitude
# appending instances to list
# list.append(geeks(2, 3))
# list.append(geeks(12, 13))
# list.append(geeks(22, 33))
 


    
            
            
                
    
    
    
def main():
    name = input("Hello! Please enter your name: \n")
    print("Welcome", name,"!")
    print()
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
                    if linked_list.searchNode(value) == True:
                        linked_list.deleteNode(indices)
                        print("Node/s deleted.")         
                else:
                    print("Please choose from the list")
                
                print()
                displayLLOptions() 
                LL_choice = input()
                
            print("You're back to main menu\n")
        
        elif choice == 2:
            st = input("Please enter your string: ")
            stack = Stack()
            stack.transformList(st)
            stack.checkPalindrome()
            
        print()    
        displayMenu()
        choice = int(input())
    print("You exited.")
            
    
main()
    
