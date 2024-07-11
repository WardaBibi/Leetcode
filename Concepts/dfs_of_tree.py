class tree:
    def __init__(self,val=0,right=None,left=None):
        self.val=val
        self.left=left
        self.right=right

class DFS:
    def InOrder(self,root):
        if root == None:
            return
        self.InOrder(root.left)
        print(root.val)
        self.InOrder(root.right)
        
    def PreOrder(self,root):
        if root == None:
            return
        print(root.val)
        self.PreOrder(root.left)
        self.PreOrder(root.right)
    
    def PostOrder(self,root):
        if root==None:
            return
        self.PostOrder(root.left)
        self.PostOrder(root.right)
        print(root.val)

root=tree(10)
root.left=tree(5)
root.right=tree(20)
root.left.left=tree(3)
root.left.right=tree(6)
root.right.left=tree(15)
root.right.right=tree(30)


dfs=DFS()
print("Pre Order: ")
dfs.PreOrder(root)

print("PostOrder: ")
dfs.PostOrder(root)

print("InOrder: ")
dfs.InOrder(root)


# time complexity: O(n) -> each node is being visited once
# space complexity: O(h) ->because of recursion at each call stack of height h would be used  where h is the height of tree , in worst case it would be O(n) when we have an unbalanced tree
 # and the height would be equal to number of nodes but in best case height would be log(n) so space complexity would be O(log(n))      
        
