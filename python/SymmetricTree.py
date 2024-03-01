
class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None
        
class CompleteBinaryTree:
    def __init__(self,rootKey):
        self.root=Node(rootKey)
        
    def insert(self,key):
        queue = [self.root]
        while queue:
            currentRoot=queue.pop(0)
            
            if not currentRoot.left:
                currentRoot.left=Node(key)
                break
            elif not currentRoot.right:
                currentRoot.right=Node(key)
                break
            else:
                queue.append(currentRoot.left)
                queue.append(currentRoot.right)
                
    def inOrder(self,root):
        if root:
            self.inOrder(root.left)
            print(root.val,end=' ')
            self.inOrder(root.right)
        
        
        

class Solution:
    def symmetric(self,left,right)->bool:
        if (not left and not right) or (left == '#' and right=='#'):
            return True
        elif (not left and right)  or (left and not right) or left.val!=right.val:
            return False
        else:
            return (self.symmetric(left.left,right.right)) and (self.symmetric(left.right,right.left))


if __name__== "__main__":
    tree=CompleteBinaryTree(2)
    tree.insert(3)
    tree.insert(3)
    tree.insert('#')
    tree.insert(1)
    tree.insert(1)
    tree.insert('#')
    
    tree.inOrder(tree.root)
    
    checkSymmetric=Solution()
    print(checkSymmetric.symmetric(tree.root.left,tree.root.right))
    
    

