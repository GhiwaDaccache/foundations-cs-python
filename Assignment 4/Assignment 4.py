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
    
def displayMatrixMenu():
    print("Please select an action from the following:",
        "\n\ta. Add vertex\n",
        "\tb. Add edge\n",
        "\tc. Remove vertex\n",
        "\td. Remove edge\n",
        "\te. Display vertices with a degree of X or more.\n",
        "\tf. Return to main menu"
        )
    
class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def addNode(self, value):
        node = Node(value)
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
        self.name = name
        self.midterm_grade = midterm_grade
        self.final_grade = final_grade
        self.good_attitude = good_attitude

class PriorityQueue:
    def __init__(self):
        self.head = None
        self.size = 0

    def displayNodes(self):
        current = self.head
        if current == None:
            print("Empty linked list")
            return 
        else:
            while current != None:
                print(current.info.name, end=" -> ")
                current = current.next  

    def addStudent(self, student):
        node = Node(student)
        if self.size == 0:
            self.head = node
            self.size += 1
        else:
            if student.good_attitude == True:
                current = self.head
                previous = self.head
                
                while current != None and node.info.final_grade < current.info.final_grade:
                    previous = current
                    current = current.next
                
                while node.info.final_grade == current.info.final_grade and node.info.midterm_grade < current.info.midterm_grade: 
                    node.next = current
                    previous.next = node
 
                node.next = current
                previous.next = node
                current = node
                self.size += 1
                    
class Graph:
    
    def __init__(self, vertices_number):
        self.vertices_number = vertices_number
        self.adj_matrix = [[0] * vertices_number for _ in range(vertices_number)]
    
    def addVertex(self):
        self.vertices_number += 1
        for _ in range(self.vertices_number):
            self.adj_matrix.append([0]*self.vertices_number)
        print("Added vertex", self.vertices_number - 1)
        
    def addEdge(self, v1, v2):  
        if 0 <= v1 < self.vertices_number and 0 <= v2 < self.vertices_number:
            self.adj_matrix[v1][v2] = 1
            self.adj_matrix[v2][v1] = 1
            print("Added an edge between", v1, "and", v2, "\n")

        else:
          print("Invalid vertex.")
          
    def removeVertex(self, vertex):
        if 0 <= vertex <= self.vertices_number: 
            del self.adj_matrix[vertex] 
            for row in self.adj_matrix:
                del row[vertex] 
            self.size -= 1 
            
    def displayGraph(self):
        if len(self.adj_matrix) == 0:
            print("The graph is empty.\n")
            return  
        for r in self.adj_matrix:
            print(" ".join(map(str, r)))
        
            
                
    
    
    
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
            
        elif choice == 5:
            vertices = 0
            graph = Graph(vertices)
            displayMatrixMenu()
            matrix_choice = input()
            
            while matrix_choice != "f":
                
                if matrix_choice == "a":
                    graph.addVertex()
                    
                if matrix_choice == "b":
                    vertex1 = input("Please enter vertex 1: ")
                    vertex2 = input("Please enter vertex 2: ")
                    graph.addEdge(vertex1, vertex2)
                
                if matrix_choice == "c":
                    vertex = input("Please enter the vertex you would like to remove: ")
                    graph.removeVertex(vertex)
                    
                
            
            
            
            
        print()    
        displayMenu()
        choice = int(input())
    print("You exited.")
            
    
main()
    
