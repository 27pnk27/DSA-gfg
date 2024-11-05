class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
        self.height=1

def inorder_traversal(root):
    if root==None:
        return []

    return inorder_traversal(root.left)+[root.data]+inorder_traversal(root.right)

def preorder_traversal(root):
    if root==None:
        return []

    return [root.data]+preorder_traversal(root.left)+preorder_traversal(root.right)


def insert(root,data):
    if(data>root.data):
        if(root.right):
            insert(root.right,data)
        else:
            root.right=Node(data)

    if (data < root.data):
        if (root.left):
            insert(root.left, data)
        else:
            root.left = Node(data)

    return root



root1=Node(2)
root1.left=Node(1)
root1.right=Node(3)

#print(inorder_traversal(insert(root1,4)))
#print(preorder_traversal(insert(root1,4)))

def search(root,data):
    if(root==None):
        return False

    if(root.data==data):
        return root

    elif(root.data<data):
        return search(root.right,data)

    else:
        return search(root.left,data)

#print(search(root1,3))


def ino_successor(root):
    curr = root.right
    while curr and curr.left:
        curr = curr.left
    return curr


def delete(root, data):
    if root is None:
        return root

    # Traverse the tree to find the node to be deleted
    if data < root.data:
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)
    else:
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children: Get the inorder successor (smallest in the right subtree)
        temp = ino_successor(root)

        # Copy the inorder successor's content to this node
        root.data = temp.data

        # Delete the inorder successor
        root.right = delete(root.right, temp.data)

    return root

def floor(root,x):
    if(root==None):
        return None
    if(x<root.data):
        return floor(root.left,x)
    elif(x==root.data):
        return root.data
    else:
        if(root.right):
            if(root.right.data<=x):
                return floor(root.right,x)
            else:
                curr=root.right
                while(curr.left):
                    curr=curr.left
                    if(curr.data<=x):
                        return curr
                return root.data

        else:
            return root.data



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

        # Return the new root
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

        # Return the new root
        return y

    def insert(self, root, data):
        # Perform the normal BST insertion
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        # Update height of this ancestor node
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        # Get the balance factor of this ancestor node to check whether
        # this node became unbalanced
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

    def min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.min_value_node(node.left)

    def delete(self, root, data):
        # Perform standard BST delete
        if not root:
            return root

        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            # Node with only one child or no child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Node with two children: Get the inorder successor
            temp = self.min_value_node(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        # Update height of the current node
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        balance = self.get_balance(root)

    def ceil(self,root, x):
        if (root == None):
            return None

        if (x > root.data):
            return self.ceil(root.right, x)

        elif (x == root.data):
            return root.data

        else:
            if (root.left):
                if (x <= root.left.data):
                    return self.ceil(root.left, x)
                else:
                    curr = root.left
                    while (curr.right):
                        if (x <= curr.data):
                            return curr.data
                    return root.data

            else:
                return root.data



l=[4,1,3,0.75,7,5,2,6,0.5]

root4=None
k=AVLTree()
for i in l:
    root4=k.insert(root4,i)

print(preorder_traversal(root4),inorder_traversal(root4))

k=k.delete(root4,2)

print(preorder_traversal(root4),inorder_traversal(root4))

def ceil_on_left(a):
    n=len(a)
    root=Node(a[0])
    avl=AVLTree()
    for i in range(1,n):
        root=avl.insert(root,i)
    print('ib',inorder_traversal(root),preorder_traversal(root))
    b=[]
    for i in a:
        b.append(avl.ceil(root,i))

    return b

print(ceil_on_left([2,8,30,15,25,12]))
















































