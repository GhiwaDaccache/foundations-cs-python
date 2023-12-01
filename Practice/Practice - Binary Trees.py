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
                    
                