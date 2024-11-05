class arr_stack:
    def __init__(self):
        self.arr=[]
        self.size=0
        self.mini=[]
    def push(self,data):
        self.arr.append(data)
        self.size+=1
        if(self.mini==[] or self.mini[-1]>=data):
            self.mini.append(data)
        return self.arr
    def peek(self):
        if(self.isempty()==False):
            return self.arr[-1]
    def pop(self):
        if(self.isempty()==False):
            self.size-=1
            if(self.mini[-1]==self.peek()):
                self.mini.pop()
            return self.arr.pop()
        else:
            raise IndexError('Stack Underflow')
    def get_size(self):
        return self.size
    def get_min(self):
        return self.mini[-1]
    def isempty(self):
        if self.size==0:
            return True
        else:
            return False
    def print(self):
        print(self.arr)
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class singlyLinkedlist_stack:
    def __init__(self):
        self.head=None
        self.size=0
    def isempty(self):
        if self.head==None:
            return True
        else:
            return False
    def push(self,data):
        self._size+=1
        if(self.head==None):
            self.head=Node(data,None)
            return
        self.head=Node(data,self.head)
    def pop(self):
        if(self.head==None):
            raise IndexError('Pop from empty stack')
        popped_node=self.head
        self.head=self.head.next
        self.size-=1
        return popped_node.data
    def peek(self):
        if self.head==None:
            raise IndexError('Peek from empty stack')
        return self.head.data
    def size(self):
        return self._size()
    def __str__(self):
        result=''
        curr=self.head
        while curr:
            result+=str(curr.data)
            curr=curr.next
        return result


def is_balanced_parenthesis(x):
    n=len(x)
    stack=arr_stack()
    for i in x:
        if(stack.isempty()):
            return False
        if(i=='(' or i=='[' or i=='{'):
            stack.push(i)
        elif(i==')'):
            if(stack.pop()!='('):
                return False
        elif (i == ']'):
            if (stack.pop() != '['):
                return False
        else:
            if (stack.pop() != '}'):
                return False
    return True



class TwoStack:
    def __init__(self,n):
        self.arr=[None]*n
        self.cap=n
        self.top1=-1
        self.top2=n

    def push1(self,x):
        if(self.top1<self.top2-1):
            self.top1+=1
            self.arr[self.top1]=x
            return True
        return False

    def push2(self,x):
        if(self.top1<self.top2-1):
            self.top2-=1
            self.arr[self.top2]=x
            return True
        return False

    def pop1(self):
        if(self.top1>=0):
            x=self.arr[self.top1]
            self.top1-=1
            return x
        return None

    def pop2(self):
        if(self.top2<self.cap):
            x=self.arr[self.top2]
            self.top2+=1
            return x
        return None

    def size1(self):
        return self.top1+1

    def size2(self):
        return self.top2-self.cap

def stock_span(a):
    n=len(a)
    stack=arr_stack()
    stack.push(0)
    t=[1]
    for i in range(1,n):
        while(stack.isempty()==False and a[stack.peek()]<=a[i]):
            stack.pop()
        if(stack.isempty()==False):
            t.append(i-stack.peek())
        else:
            t.append(i+1)
        stack.push(i)
    return t


#print(stock_span([60,10,20,15,35,50,70]))

def prev_greater_element(a):
    n=len(a)
    t=[-1]
    stack=arr_stack()
    stack.push(a[0])
    for i in range(1,n):
        while(stack.isempty()==False and a[i]>=stack.peek()):
            stack.pop()
        if(stack.isempty()==True):
            t.append(-1)
        else:
            t.append(stack.peek())
        stack.push(a[i])
    return t

#print(prev_greater_element([15,10,18,12,4,6,2,8]))

def next_greater_element(a):
    a=a[::-1]
    k=prev_greater_element(a)
    k=k[::-1]
    return k

#print(next_greater_element([10,15,20,25]))

def prev_small_element(a):
    n=len(a)
    t=[-1]
    stack=arr_stack()
    stack.push(a[0])
    for i in range(1,n):
        while(stack.isempty()==False and a[stack.peek()]>=a[i]):
            stack.pop()
        if(stack.isempty()==True):
            t.append(-1)
        else:
            t.append(stack.peek())
        stack.push(i)
    return t

#print(prev_small_element([6,2,5,4,1,5,6]))

def next_small_element(a):
    n=len(a)
    t=[n]*n
    stack=arr_stack()
    stack.push(n-1)
    for i in range(n-2,-1,-1):
        while(stack.isempty()==False and a[stack.peek()]>=a[i]):
            stack.pop()
        if(stack.isempty()==False):
            t[i]=stack.peek()
        stack.push(i)
    return t

#print(next_small_element([6,2,5,4,1,5,6]))

def largest_rect_area1(a):
    n=len(a)
    next_small=next_small_element(a)
    prev_small=prev_small_element(a)
    res=0
    curr=0
    for i in range(n):
        res=max(res,(next_small[i]-prev_small[i]-1)*a[i])
    return res

#print(largest_rect_area([6,2,5,4,5,1,6]))

def largest_rect_area2(a):
    n=len(a)
    stack=arr_stack()
    res=0
    for i in range(n):
        while(stack.isempty()==False and a[i]<=a[stack.peek()]):
            k=stack.pop()
            if(stack.isempty()):
                res=max(res,a[k]*i)
            else:
                res=max(res,(i-stack.peek()-1)*a[k])
        stack.push(i)

    while(not stack.isempty()):
        k=stack.pop()
        if stack.isempty():
            res=max(res,n*a[k])
        else:
            res = max(res, (n - stack.peek() - 1) * a[k])

    return res

print(largest_rect_area2([6,2,5,4,5,1,6]))

def largest_rect_ones(a):
    n=len(a)
    m=len(a[0])
    t=a[0]
    res=0
    for i in range(1,n):
        for j in range(m):
            if(a[i][j]==1):
                t[j]+=1
            else:
                t[j]=0
        res=max(res,largest_rect_area2(t))
    return res


#print(largest_rect_ones([[1,0,0,1,1],[0,0,0,1,1],[1,1,1,1,1],[0,1,1,1,1]]))

s=arr_stack()
s.push(10)
s.push(20)
s.push(3)
s.push(5)
s.push(15)
s.push(30)
s.push(2)
#print(s.get_min())
s.pop()
s.pop()
s.pop()
#print(s.get_min())



def infix_to_postfix(a):
    dicti={'^':3,'*':2,'/':2,'+':1,'-':1}
    stack=[]
    s=''
    for i in a:
        if(i=='('):
            stack.append(i)
        elif(i==')'):
            while(stack[-1]!='(' and stack):
                s+=stack.pop()
            stack.pop()
        elif(i=='^'):
            stack.append(i)
        elif(i=='*' or i=='/' or i=='+' or i=='-'):
            while(stack and stack[-1]!='('):
                if(dicti[stack[-1]]>=dicti[i]):
                    s+=stack.pop()
                else:
                    break
            stack.append(i)
        else:
            s+=i
    while stack:
        s+=stack.pop()
    return s

#print(infix_to_postfix("a^b^c"))

def postfix_eval(a):
    a = list(a.split(' '))
    operators = {'+', '-', '/', '*', '^'}
    while len(a) > 1:
        #print(a)
        for i in range(len(a)):
            if a[i] in operators:
                if a[i] == '^':
                    a[i-2] = str(float(a[i-2]) ** float(a[i-1]))
                elif a[i] == '*':
                    a[i-2] = str(float(a[i-2]) * float(a[i-1]))
                elif a[i] == '/':
                    a[i-2] = str(float(a[i-2]) / float(a[i-1]))
                elif a[i] == '+':
                    a[i-2] = str(float(a[i-2]) + float(a[i-1]))
                else:
                    a[i-2] = str(float(a[i-2]) - float(a[i-1]))
                a.pop(i-1)
                a.pop(i-1)
                break
    return float(a[0])

#print(postfix_eval('5 9 8 + 4 6 * / 7 - -'))

def infix_to_prefix(a):
    dicti={'^':3,'/':2,'*':2,'+':1,'-':1}
    stack=[]
    s=''
    n=len(a)
    for i in range(n-1,-1,-1):
        if(a[i]==')'):
            stack.append(a[i])
        elif(a[i]=='('):
            while(stack[-1]!=')'):
                s+=stack.pop()
            stack.pop()
        elif(a[i]=='^'):
            stack.append(a[i])
        elif(a[i]=='*' or a[i]=='/' or a[i]=='+' or a[i]=='-'):
            while(stack and stack[-1]!=')'):
                if(dicti[stack[-1]]>=dicti[a[i]]):
                    s+=stack.pop()
                else:
                    break
            stack.append(a[i])
        else:
            s+=a[i]

    while(stack):
        s+=stack.pop()

    return s[::-1]

print(infix_to_prefix('(3+5)*(6-2)/(4^2)+7-9'))












































































    



































































































