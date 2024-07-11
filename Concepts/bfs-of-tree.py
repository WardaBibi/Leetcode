import collections
class Tree:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right



def bfs(root):
    if root == None:
        return -1
    queue=collections.deque()
    results=[]
    queue.append(root)
    while queue:
        level=[]
        length_lev=len(queue)
        
        for i in range(length_lev):
            node = queue.popleft()
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        if level: 
            results.append(level)
    return results
                
 
root= Tree(3)
root.left=Tree(4)
root.right=Tree(6)
root.left.left=Tree(2)
root.left.right=Tree(0)
root.right.right=Tree(9)

print(bfs(root))
