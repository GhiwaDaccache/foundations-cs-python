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
# We create a new node by initiating class node with next pointing to none(still not in linked list), and setting info as parameter to pass to the node. 
    def __init__(self, info):
        self.info = info
        self.next = None

class LinkedList:
    def __init__(self):
# We initiate class linked list by setting the head and tail to none since it's still empty.
# And for the same reason we set size = 0.
        self.head = None
        self.tail = None
        self.size = 0
        
    def addNode(self, value): # O(1) because it takes a constant of time to update the head and tail of a linked list.
        node = Node(value)
# To add a node to the linked list, we first check if the list is empty by accessing self.size.
# If it's the case we set the node as the head and tail of the list and increase the size by 1. 
        if self.size == 0:
            self.head = node
            self.tail = node
            self.size += 1
            
# If the list is not empty, we add the node by changing the next of the tail. It now points to the node, and the node is the new tail.
# We also increase the size by 1. 
        else:
            self.tail.next = node
            self.tail = node
            self.size += 1
            
    def displayNodes(self): #O(N) N being the number of nodes, because the function loops through the linked list.
# The current variable starts at the head of the list, if it's none it'll state that the list is empty.
# Otherwise it'll loop through the whole list and print the info of each node until it reaches None (the end of the list).
        current = self.head
        if current == None:
          print("Empty linked list")
          return 
        else:
          while current != None:
              print(current.info, end=" -> ")
              current = current.next
          print(None)
          
          
    def searchNode(self, value): # O(N) N being the number of nodes, because the function loops through the linked list.
# The if statement checks if the list is empty by checking the size of the list.
        global indices
        indices = []
        if self.size != 0:
            index = 0
            current = self.head
# This loop, will itirate through the whole list checking if the info of each node is equal to the given value, until it reaches the end of the list where current will be None.
# The index variable keeps track of the order of the nodes, which will increase by 1 after each loop. 
# Whenever the value matches the info, it'll append the index of the node to a list.

            while current != None:
                if current.info == value:
                    indices.append(index)
                current = current.next
                index += 1
        
        else:
          print("List is empty")
          return False
# If the function returns False (Empty list or value not found), it will not call the deleteNode() method.      
        if len(indices) == 0:
          print("The value is not in the list")
          return False
        return True
    

    def deleteNode(self, index_list): #O(N^2) in the for loop N is the length of index list and in the while loop N is the number of nodes.
        current = self.head
        previous = self.head
        loop_index = 0
# The linked list will have two variables pointing to the nodes, current and previous. 
# As well as the loop index, that will keep track of the node order. 
# Then for each element in the index list, we will delete the corresponding node.
        for x in index_list:
# Whereas this while loop will itirate through the linked list as long as the loop index is not the same as the index in index list and the end of the list is not reached. 
            while loop_index != x and current.next != None:
                previous = current
                current = current.next
                loop_index += 1    
# When the loop index matches the index in the list and it's the head of the list:
# We change the head to become the next node. 
# And set the next of current (old head) to point to None.
# lastly, we update current and previous to point to the new head to continue the loop. And decrease size by 1.               
            if loop_index == x and current == self.head:   
                self.head = self.head.next
                current.next = None
                current = self.head
                previous = self.head
                self.size -= 1
                loop_index +=1
 
# When the loop index matches the index in the list and it's in the middle of the list: 
# We set the next of previous to point to the next node of the one we're trying to delete. 
# And current becomes the next node.
# Without forgetting to always decrease size.                
            elif loop_index == x and current.next != None:   
                previous.next = current.next
                current = current.next
                self.size -= 1
                loop_index +=1
                
# When the loop index matches the index in the list and it's at the end of the list:
# We "detach" the last node from the list by pointing the next of previous to None. 
# And update tail to previous. 
            elif loop_index == x and current.next == None:
                previous.next = None
                self.tail = previous
                self.size -= 1
  
class Stack:
    def __init__(self):
# We create a stack by initializing an empty list of size 0.
        self.elements = []
        self.size = 0

    def push(self, value): #O(1) it takes a constant amount of time to append to a list.
# The push method add an element to the stack by appending each element passed as parameter to the list. 
        self.elements.append(value)
        self.size += 1
    
    def transformList(self, string): #O(N) N being the length of the string. 
# This method converts a string to a list by pushing every character of the string to the stack.
        for x in string:
            self.push(x)
    
    def peek(self): #O(1) it only checks the last element of the stack. 
# If the stack is not empty, it'll return the last element in the list to compare with the first.
        if self.size == 0:
            print("Empty stack.")
        else:
            return self.elements[len(self.elements) - 1]
    
    def peekReverse(self): #O(1) it only checks the first element of the stack.
# If the stack is not empty, it'll return the first element in the list to compare with the last.    
        if self.size == 0:
            print("Empty stack.")
        else:
            return self.elements[0]
    
    def pop(self): #O(1) it deletes the last element of the stack.
# This function is only called if the first and last element of the stack are the same. 
# If the stack is not empty, it'll remove the last element of the stack.
        if self.size == 0: 
            print("Empty stack.")
        else:
            self.elements = self.elements[:-1]
            self.size -= 1
    
    def dequeue(self): #O(1) it deletes the first element of the stack.
# This function is only called if the first and last element of the stack are the same. 
# If the stack is not empty, it'll remove the first element of the stack.
        if self.size == 0: 
            print("Empty stack.")
        else:
            self.elements = self.elements[1: ]
            self.size -= 1
    
    def checkPalindrome(self): #O(N) N being half the length of the list.
# We start by looping through half of the list, because each time the condition checks out 
        for i in range(len(self.elements) //2):
            while self.size > 1:
                if self.peek() == self.peekReverse():
                    self.pop()
                    self.dequeue()
                
                else:
                    print("The string is not a palindrome")
                    return False

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
        for row in self.adj_matrix:
            row.append(0)
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
            self.vertices_number -= 1 
            
    def removeEdge(self, v1, v2):  
        if 0 <= v1 < self.vertices_number and 0 <= v2 < self.vertices_number and self.adj_matrix[v1][v2] == self.adj_matrix[v2][v1] == 1 :
            self.adj_matrix[v1][v2] = 0
            self.adj_matrix[v2][v1] = 0
            print("Removed the edge between", v1, "and", v2, "\n")
        elif 0 > v1 > self.vertices_number or 0 > v2 > self.vertices_number:
            print("Invalid vertex ")
        elif self.adj_matrix[v1][v2] == self.adj_matrix[v2][v1] != 1: 
            print("No edge exists between vertices")
            
    def displayGraph(self):
        if len(self.adj_matrix) == 0:
            print("The graph is empty.\n")
            return  
        for r in self.adj_matrix:
            print(" ".join(map(str, r)))
            
    def displayVertices(self):
        pass
            
                
    
    
    
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
                        print()
                        linked_list.displayNodes()
                        print()
                else:
                    print("Please choose from the list")
                
                print()
                displayLLOptions() 
                LL_choice = input()
                
            print("You're back to main menu\n")
        
        elif choice == 2:
            st = input("Please enter your string: ")
            stack = Stack()
            stack.transformList(st.lower())
            if stack.checkPalindrome() != False:
                print("The string is a palindrome")
            
        elif choice == 5:
            vertices = int(input("Enter the number of vertices: "))
            graph = Graph(vertices)
            displayMatrixMenu()
            matrix_choice = input()
            
            while matrix_choice != "f":
                
                if matrix_choice == "a":
                        graph.addVertex()
                        print()
                        graph.displayGraph()
                        print()
                    
                elif matrix_choice == "b":
                    vertex1 = int(input("Please enter vertex 1: "))
                    vertex2 = int(input("Please enter vertex 2: "))
                    graph.addEdge(vertex1, vertex2)
                    print()
                    graph.displayGraph()
                    print()
                
                elif matrix_choice == "c":
                    vertex = int(input("Please enter the vertex you would like to remove: "))
                    graph.removeVertex(vertex)
                    print()
                    graph.displayGraph()
                    print()
                
                elif matrix_choice == "d":
                    vertex_a = int(input("Please enter vertex 1: "))
                    vertex_b = int(input("Please enter vertex 2: "))
                    graph.removeEdge(vertex_a, vertex_b) 
                    print()
                    graph.displayGraph()
                    print()
                    
                else:
                    print("Please choose from the list")
                
                print()
                displayMatrixMenu() 
                matrix_choice = input()
                
            print("You're back to main menu\n")
                    
                
                    
                
            
            
            
            
        print()    
        displayMenu()
        choice = int(input())
    print("You exited.")
            
    
main()
    
