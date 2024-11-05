


class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

    def show(self):
        if(self.left!=None):
            print(self.left.data,end=' ')
        print(self.data,end=' ')
        if(self.right!=None):
            print(self.right.data)

def inorder_traversal(root):
    if(root!=None):
        inorder_traversal(root.left)
        print(root.data,end=' ')
        inorder_traversal(root.right)



root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)
root.right.right=Node(70)

#print(inorder_traversal(root))

def preorder_traversal(root):
    if(root!=None):
        print(root.data, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)


#print(preorder_traversal(root))

def postorder_traversal(root):
    if(root!=None):

        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=' ')

#print(postorder_traversal(root))

def height(root):
   if(root==None):
       return 0
   else:
       return max(height(root.left),height(root.right))+1

#print(height(root))

def print_at_k(root,k):
    if(root==None):
        return
    if(k==0):
        print(root.data,end=' ')
    else:
        print_at_k(root.left,k-1)
        print_at_k(root.right,k-1)

#print(print_at_k(root,2))


def level_order_traversal1(root):
    t=height(root)
    for i in range(t):
        if(print_at_k(root,i)!=None):
            print(print_at_k(root,i))

def level_order_traversal2(root):
    t=[]
    t.append(root)
    while(t):
        #print(t)
        curr=t[0]
        t.pop(0)
        print(curr.data,end=' ')
        if(curr.left!=None):
            t.append(curr.left)
        if(curr.right!=None):
            t.append(curr.right)


root1=Node(70)
root1.left=Node(50)
root1.left.left=Node(40)
root1.left.right=Node(60)
root1.right=Node(90)
root1.right.left=Node(80)
root1.right.right=Node(100)

#print(level_order_traversal2(root1))
#print(inorder_traversal(root1))


def level_order_traversal_lbl(root):
    t=[root,None]
    while len(t)>1:
        curr=t[0]
        t.pop(0)
        if(curr!=None):
            print(curr.data,end=' ')
        else:
            print(' ')
            t.append(None)
            continue
        if(curr.left!=None):
            t.append(curr.left)
        if(curr.right!=None):
            t.append(curr.right)

#print(level_order_traversal_lbl(root1))

def level_order_traversal3(root):
    q = [root]
    t = []
    while q:
        count = len(q)
        k = []
        for i in range(count):
            curr = q.pop(0)
            k.append(curr.data)
            if (root.left):
                q.append(root.left)
            if (root.right):
                q.append(root.right)

        t.append(k)

    return t

def tree_size(root):
    if(root==None):
        return 0
    else:
        return 1+tree_size(root.left)+tree_size(root.right)

#print(tree_size(root1))

def max_tree(root):
    if(root==None):
        return -float('inf')
    else:
        return max(root.data,max_tree(root.left),max_tree(root.right))


#print(max_tree(root1))

def left_view_tree(root):
    if root is None:
        return
    q = [root]
    while q:
        count = len(q)
        for i in range(count):
            curr = q.pop(0)  # Pop the first element in the queue
            if i == 0:
                print(curr.data,end=' ')  # Print the first node of this level
            if curr.left is not None:
                q.append(curr.left)  # Append the left child of curr
            if curr.right is not None:
                q.append(curr.right)
        # Append the right child of curr


#print(left_view_tree(root1))

def children_sum(root):
    if(root==None):
        return True
    if(root.left==None and root.right==None):
        return True
    sum=0
    if(root.left):
        sum+=root.left.data
    if(root.right):
        sum+=root.right.data

    return sum==root.data and children_sum(root.left) and children_sum(root.right)

root2=Node(20)
root2.left=Node(8)
root2.right=Node(12)
root2.left.left=Node(3)
root2.left.right=Node(5)

#print(children_sum(root2))

def balanced_tree(root):
    if(root==None):
        return 0
    lh=balanced_tree(root.left)
    if(lh==-1):
        return -1
    rh=balanced_tree(root.right)
    if(rh==-1):
        return -1
    if(abs(lh-rh)>1):
        return -1
    else:
        return max(lh,rh)+1

root3=Node(8)
root3.left=Node(12)
root3.right=Node(15)
root3.right.right=Node(16)
root3.right.right.right=Node(17)
root3.left.left=Node(13)
root3.left.right=Node(14)


#print(balanced_tree(root3))

def max_width(root):
    q=[root,None]
    res=0
    while len(q)>1:
        curr=q[0]
        q.pop(0)
        if(curr==None):
            res=max(res,len(q))
            q.append(None)
            continue
        if(curr.left):
            q.append(curr.left)
        if(curr.right):
            q.append(curr.right)
        #print(q)

    return res

#print(max_width(root2))

pre_index=0
def construct_bintree(pre,ino):
    if not pre:
        return None

    root=Node(pre[0])
    mid=ino.index(pre[0])
    root.left=construct_bintree(pre[1:mid+1],ino[:mid])
    root.right=construct_bintree(pre[mid+1:],ino[mid+1:])

    return root

#print(inorder_traversal(construct_bintree([10,20,30,40,50],[20,10,40,30,50])))
#print(preorder_traversal(construct_bintree([10,20,30,40,50],[20,10,40,30,50])))

def zigzag_traverse1(root):
    q=[root]
    stack=[]
    reverse=False
    while q:
        count=len(q)
        for i in range(count):
            curr=q.pop(0)
            if not reverse:
                print(curr.data,end=' ')
            else:
                stack.append(curr.data)
            if(curr.left!=None):
                q.append(curr.left)
            if(curr.right!=None):
                q.append(curr.right)
        if reverse:
            while stack:
                print(stack.pop(),end=' ')
        reverse=not reverse


root4=Node(10)
root4.left=Node(20)
root4.right=Node(30)
root4.right.left=Node(40)
root4.right.right=Node(50)
root4.right.left.left=Node(60)
root4.right.left.right=Node(70)
root4.right.right.right=Node(80)

#print(zigzag_traverse1(root4))

def zigzag_traverse2(root):
    stack1=[root]
    stack2=[]
    reverse=True
    while stack1 or stack2:
        #print(reverse)
        if (reverse==True):
            count1=len(stack1)
            for i in range(count1):
                curr=stack1.pop()
                print(curr.data,end=' ')
                if(curr.left):
                    stack2.append(curr.left)
                if(curr.right):
                    stack2.append(curr.right)
        else:
            count2=len(stack2)
            for i in range(count2):
                curr=stack2.pop()
                print(curr.data,end=' ')
                if(curr.right):
                    stack1.append(curr.right)
                if(curr.left):
                    stack1.append(curr.left)

        reverse = not reverse

#print(zigzag_traverse2(root4))

def diameter1(root):
    if root==None:
        return None
    else:
        return max(height(root.left.left)+height(root.left.right)+1,height(root.left)+height(root.right)+1,height(root.right.left)+height(root.right.right)+1)


root12=Node(11)
root12.left=Node(10)
root12.right=Node(12)

root13=Node(1)
root13.left=Node(2)
root13.right=Node(3)
root13.right.right=Node(7)
root13.left.left=Node(4)
root13.left.right=Node(5)
root13.left.right.left=Node(6)
print(diameter1(root12))

print(postorder_traversal(root13))

root5=Node(10)
root5.left=Node(20)
root5.right=Node(30)
root5.right.left=Node(40)
root5.right.left.left=Node(60)
root5.right.right=Node(50)

#print(diameter1(root5))

def preorder_traversal_list(root):
    if root is None:
        return []
    # Visit root, then left, then right
    return [root.data] + preorder_traversal_list(root.left) + preorder_traversal_list(root.right)

def inorder_traversal_list(root):
    if root is None:
        return []
    # Visit left, then root, then right
    return inorder_traversal_list(root.left) + [root.data] + inorder_traversal_list(root.right)

def lca(node1,node2,root):
    ino=inorder_traversal_list(root)
    mid=ino.index(root.data)
    try:
        a=ino.index(node1)
        b=ino.index(node2)
    except:
        return None
    if(a>b):
        a,b=b,a
    if(a<=mid<=b):
        return ino[mid]

    elif(a<b<mid):
        return lca(node1,node2,root.left)
    else:
        return lca(node1,node2,root.right)


root6=Node(10)
root6.left=Node(20)
root6.right=Node(30)
k=root6.right
k.left=Node(40)
k.left.left=Node(60)
k.right=Node(50)
k.right.left=Node(70)
k.right.right=Node(80)

#print(lca(60,70,root6))

#print(lca(80,100,root6))

def nodes_in_complete_bintree(root):
    left_curr=root
    right_curr=root
    t=0
    while(left_curr and right_curr):
        left_curr=left_curr.left
        right_curr=right_curr.right
        t+=1

    if(left_curr==None and right_curr==None):
        return 2**(t)-1
    elif(left_curr!=None and right_curr==None):
        return nodes_in_complete_bintree(root.left)+nodes_in_complete_bintree(root.right)+1




root7=Node(10)
root7.left=Node(20)
root7.right=Node(30)
root7.right.left=Node(60)
root7.right.right=Node(70)
root7.left.left=Node(40)
root7.left.left.left=Node(80)
root7.left.right=Node(50)
root7.left.left.right=Node(90)
root7.left.left.right.left=Node(110)
root7.left.right.left=Node(100)

root8=Node(10)
root8.left=Node(20)
root8.right=Node(30)
root8.left.left=Node(40)
root8.left.right=Node(50)
root8.right.left=Node(60)
root8.right.right=Node(70)

#print(nodes_in_complete_bintree(root7))
#print(nodes_in_complete_bintree(root8))

def serialize(root):
    if not root:
        return None

    stack = [root]
    l = []

    while stack:
        t = stack.pop()

        # If current node is NULL, store marker
        if not t:
            l.append(-1)
        else:
            # Else, store current node
            # and recur for its children
            l.append(t.data)
            stack.append(t.right)
            stack.append(t.left)

    return l

def find_node(root,value):
    if(root==None):
        return None
    if(root.data==value):
        return root

    left_result=find_node(root.left,value)
    if left_result:
        return left_result

    return find_node(root.right,value)

#print(find_node(root7,70))


def is_identical(root1, root2):
    if (not root1 and not root2):
        return True

    if (not root1 or not root2):
        return False

    return root1.data == root2.data and is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right)



root9=Node(10)
root9.left=Node(20)
root9.right=Node(30)
root9.left.left=Node(40)
root9.left.right=Node(50)
root9.right.right=Node(60)


def serialize1(root):
    q = [root]
    t = []
    while q:
        curr = q.pop(0)
        if(curr!=-1):
            t.append(curr.data)
        else:
            t.append(-1)
        if(curr==-1):
            continue
        if(curr.left):
            q.append(curr.left)
        else:
            q.append(-1)
        if(curr.right):
            q.append(curr.right)
        else:
            q.append(-1)


    return t

root13=Node(None)

print(serialize1(root13))

def iter_inorder(root):
    stack=[root]
    curr=root
    l=[]
    while curr.left:
        curr=curr.left
        stack.append(curr)

    while stack:
        curr=stack.pop()
        l.append(curr.data)
        if(curr.right):
            x=curr.right
            stack.append(x)
            curr=curr.right
            while curr.left:
                curr = curr.left
                stack.append(curr)

    return l

def iter_preoder(root):
    if(root==None):
        return []
    stack=[root]
    l=[]
    while stack:
        curr=stack.pop()
        l.append(curr.data)
        if(curr.right):
            stack.append(curr.right)
        if(curr.left):
            stack.append(curr.left)

    return l

#print(iter_preoder(root7))
#print(is_identical(root1,root1))


def flip(root):
    if(root==None):
        return None

    root.left,root.right=root.right,root.left

    flip(root.left)
    flip(root.right)

    return root



#print(inorder_traversal_list(flip(root9)))


def complete_bintree(root, k):
    if (k == 0):
        return root

    if not root.left:
        root.left = Node(-1)

    if not root.right:
        root.right = Node(-1)

    complete_bintree(root.left, k - 1)
    complete_bintree(root.right, k - 1)

    return root




root10=Node(10)
root10.left=Node(7)
root10.left.right=Node(9)
root10.right=Node(15)
root10.right.left=Node(11)

#print(inorder_traversal_list(complete_bintree(root10,height(root10)-1)))

#print(inorder_traversal_list(flip(complete_bintree(root10,height(root10)-1))))


def level_order_traversal4(root):
    q = [root]
    t = []
    while q:
        count = len(q)
        k = []
        for i in range(count):
            curr = q.pop(0)
            k.append(curr.data)
            if (curr.left):
                q.append(curr.left)
            if (curr.right):
                q.append(curr.right)

        t.append(k)

    return t
#print(level_order_traversal4(complete_bintree(root10,height(root10)-1)))

k=flip(root10)
#print(level_order_traversal4(complete_bintree(k,height(root10)-1)))

def pos(val, root):
    if (root == None):
        return None

    if (val == root.data):
        return 0

    if(root.left and val==root.left.data):
        return -1

    if(root.right and val==root.right.data):
        return 1

    lp=pos(val,root.left)

    if(lp):
        return lp-1

    rp=pos(val,root.right)

    if(rp):
        return rp+1

    return None

root11=Node(4)


#print(pos(11,root10))

def single(root):
    res = [[root]]
    if not root.left and not root.right:
        return res
    temp = res.pop()

    if temp[-1].left:
        k = temp[:]
        k.append(temp[-1].left)
        res.append(k)

    if temp[-1].right:
        k = temp[:]
        k.append(temp[-1].right)
        res.append(k)

    return res

x=single(root7)
for i in range(len(x)):
    for j in range(len(x[i])):
        x[i][j]=x[i][j].data

print(x)










































    



















































































