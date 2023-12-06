##########
# Practice
##########

# Binary Tree implementation:
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, info):
        node = Node(info)
        
        if self.root == None:
            self.root = node
            print("Added", node.value, "as the root node.")
        
        else:
            queue = [self.root]
            while queue:
                current = queue.pop(0)
                
                if current.left == None:
                    current.left = node
                    print("Added", node.value, "as the left child of", current.value)
                    print()
                    return
                
                elif current.right == None:
                    current.right = node
                    print("Added", node.value, "as the right child of", current.value)
                    print()
                    return
                
                else:
                    queue.append(current.left)
                    queue.append(current.right)
                    print("Added", current.left.value, "and", current.right.value, "to the queue.")
                    print()
            
    def printTree(self,current):
        if current != None:
          print(current.value) # For pre-order
          self.printTree(current.left)
          # print(current.data) # For in-order
          self.printTree(current.right)
          # print(current.data) # For post-order

# Test example
# tree = BinaryTree()
# values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# for x in values:
#     tree.insert(x)
# tree.printTree(tree.root)


# Binary Tree implementation from list (parent [i], left child [2i], right child [2i +1]):
    def convertListToTree(self, lst):
        nodes = []
        for val in lst:
          if val != None:
            nodes.append(Node(val))
          else:
            nodes.append(None) 
      
        for i in range(1, (len(lst) -1)):
            
          if nodes[i] != None:
              
            if (len(lst) - 1) >= 2*i:
              nodes[i].left = nodes[2*i]
            else:
              None
              
            if (len(lst) -1) >= (2*i +1):
              nodes[i].right = nodes[2*i +1]
            else:
              None
                  
    
# Test example
# values = [None, 5, 7, 2, 4, 3, 14, None, None, None, 6, 1, None, 8, None, None, None, None, None, None, None, None, None, None, None, None, 7]
# tree2 = BinaryTree()
# tree2.convertListToTree(values)
# print("Binary Tree from List:")
# tree2.display_list()

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insertBST(self, value):
        node = Node(value)
        
        if self.root == None:
            self.root = node
        
        else:
            current = self.root
            while current != None:
                
                if node.value < current.value:
                    if current.left == None:
                        current.left = node
                        current = None
                    else:
                        current = current.left
                    
                elif node.value >= current.value:
                    if current.right == None:
                        current.right = node
                        current = None
                    else:
                        current = current.right
   
    def printTree(self,current):
        if current != None:
          print(current.value) # For pre-order
          self.printTree(current.left)
          # print(current.data) # For in-order
          self.printTree(current.right)
          # print(current.data) # For post-order
          

    def checkBinary(self, node):
        if node == None:
          return True
          
        if node.left != None and node.value < node.left.value:
            return False
    
        if node.right != None and node.value > node.right.value:
            return False
    
        self.checkBinary(node.left)
        self.checkBinary(node.right)
        return True
    
    def searchBST(self, value):
        if self.root == None:
            print("Empty tree.")
        else:
            current = self.root
            while current != None:
                if current.value == value:
                    return True 
                elif value >= current.value:
                    current = current.right
                elif value < current.value:
                    current = current.left
            return False
                    
        
# Test example
# bst = BinarySearchTree()
# bst.insertBST(10)
# bst.insertBST(5)
# bst.insertBST(13)
# bst.insertBST(4)
# bst.insertBST(7)
# bst.insertBST(2)
# bst.insertBST(9)
# bst.insertBST(11)
# bst.insertBST(6)
# bst.insertBST(4.0)
# bst.printTree(bst.root)
# bst.checkBinary(bst.root)
# print(bst.searchBST(5))
# print(bst.searchBST(17))


             
# coming ex:
# searching
# sorting 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    