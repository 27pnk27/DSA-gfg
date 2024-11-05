class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        # Return new root
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        # Return new root
        return y

    def insert(self, root, data):
        # Perform normal BST insertion
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        # Update the height of the ancestor node
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        # Get the balance factor to check whether this node became unbalanced
        balance = self.get_balance(root)

        # If the node is unbalanced, then there are 4 cases

        # Left Left Case
        if balance > 1 and data < root.left.data:
            return self.rotate_right(root)

        # Right Right Case
        if balance < -1 and data > root.right.data:
            return self.rotate_left(root)

        # Left Right Case
        if balance > 1 and data > root.left.data:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Right Left Case
        if balance < -1 and data < root.right.data:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        # return the (unchanged) node pointer
        return root

    def preorder(self, root):
        if not root:
            return []
        return [root.data]+self.preorder(root.left)+self.preorder(root.right)

    def inorder(self,root):
        if not root:
            return []
        return self.inorder(root.left) +[root.data] +  self.inorder(root.right)

def preorder(root):
    if not root:
        return []
    return [root.data]+preorder(root.left)+preorder(root.right)

def inorder(root):
    if not root:
        return []
    return inorder(root.left) +[root.data] +inorder(root.right)

def inorder_node(root):
    nodes = []
    if root:
        nodes.extend(inorder_node(root.left))
        nodes.append(root)
        nodes.extend(inorder_node(root.right))
    return nodes

# Example usage:
avl_tree = AVLTree()
root = None

data_list = [10, 20, 30, 40, 50, 25]

for data in data_list:
    root = avl_tree.insert(root, data)

b=[2,89,13,44,1,5,8,4]

# Preorder traversal of the AVL tree
for i in b:
    root=avl_tree.insert(root,i)
#print(avl_tree.preorder(root),avl_tree.inorder(root))
def ceil(root,x):
    if(root==None):
        return None

    if(x>root.data):
        return ceil(root.right, x)

    elif(x==root.data):
        return root.data

    else:
        if(root.left):
            if(x<=root.left.data):
                return ceil(root.left,x)
            else:
                curr=root.left
                while(curr.right):
                    if(x<=curr.data):
                        return curr.data
                return root.data

        else:
            return root.data
def left_ceil(a):
    tree=AVLTree()
    root=None
    b=[]
    for i in a:
        if(root==None):
            b.append(-1)
        elif(ceil(root,i)):
            b.append(ceil(root,i))
        else:
            b.append(-1)

        root=tree.insert(root,i)


    return b

def check_for_bst(root):
    a=inorder(root)
    b=inorder_node(root)
    n=len(a)
    for i in range(1,n):
        if(a[i]<a[i-1]):
            return False
    return True





root2=Node(1)
root2.left=Node(2)

#print(check_for_bst(root2))

def fix_bst(root):
    a=inorder_node(root)
    n=len(a)
    p1=None
    p2=None
    #print(a)
    for i in range(1,n):
        if(a[i].data<a[i-1].data):
            if not p1:
                p1=a[i-1]
            p2=a[i]
    temp=p1.data
    p1.data=p2.data
    p2.data=temp

    return root

root3=Node(20)
root3.left=Node(60)
root3.left.left=Node(4)
root3.left.right=Node(10)
root3.right=Node(80)
root3.right.left=Node(8)
root3.right.right=Node(100)
root3=fix_bst(root3)
#print(inorder(root3))

def pair_sum(root,x):
    a=inorder(root)
    n=len(a)
    i=0
    j=n-1

    while(j>=i):
        if(a[i]+a[j]<x):
            i+=1
        elif(a[i]+a[j]>x):
            j-=1
        else:
            return True
    return False

#print(pair_sum(root3,181))

def vert_sum(root):
    if not root:
        return []

    q = [root]
    posq = [0]
    maxi = float('-inf')
    mini = float('inf')

    # Dictionary to store the vertical sums
    vertical_sums = {}

    while q:
        curr = q.pop(0)
        current_pos = posq.pop(0)

        # Update the mini and maxi
        maxi = max(maxi, current_pos)
        mini = min(mini, current_pos)

        # Update the vertical sum for the current horizontal distance
        if current_pos in vertical_sums:
            vertical_sums[current_pos] += curr.data
        else:
            vertical_sums[current_pos] = curr.data

        # Traverse the left and right children
        if curr.left:
            q.append(curr.left)
            posq.append(current_pos - 1)
        if curr.right:
            q.append(curr.right)
            posq.append(current_pos + 1)

    # Create the result list from the dictionary
    result = []
    for i in range(mini, maxi + 1):
        result.append(vertical_sums[i])

    return result


root4=Node(10)
root4.left=Node(15)
root4.right=Node(25)
root4.left.left=Node(35)
root4.left.left.left=Node(40)
root4.left.right=Node(20)
root4.left.right.right=Node(75)
root4.left.right.right.right=Node(80)

print(vert_sum(root4))




























































