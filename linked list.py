#Create Nodes
#Create Linked list
#Add nodes to linked list

class Person:
    name='Harry'
    occupation='Software Developer'
    networth=10
    def info(self):
        print(f'{self.name} is a {self.occupation}')
    def __init__(self,n,o):
        print('Hey fuck you')
        self.name=n
        self.occupation=o

#Person('Jerk','Nigga').info()


#a=Person('noi','ngxf')

#print(Person.occupation)

Person.occupation='Accountant'
#print(Person.occupation)
#Person('ujd','mhtd').info()
#Person('hf','k v').info()

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class singly_LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        self.head=Node(data, self.head)


    def print(self):
        if(self.head is None):
            print('linked list is empty')
            return
        itr = self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+'->'
            itr=itr.next
        #llstr+='None'
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    def insert_values(self,datalist):
        self.head=Node(datalist[0],None)
        itr=self.head
        for i in range(1,len(datalist)):
            while itr.next:
                itr=itr.next
            itr.next=Node(datalist[i],None)

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    def remove_at(self,ind):
        if(ind==0):
            self.head=self.head.next
            return
        i=0
        itr=self.head
        while itr:
            if i==ind-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            i+=1
    def insert_at(self,ind,data):
        if(ind==0):
            self.head=Node(data,self.head)
        i=0
        itr=self.head
        while itr:
            if(i==ind-1):
                itr.next=Node(data,itr.next)
                break
            itr=itr.next
            i+=1

    def search(self,x):
        itr=self.head
        i=0
        while itr:
            #print(itr.data)
            itr = itr.next
            i+=1
            if(itr.data==x):
                return i
    def middle(self):
        t=self.get_length()/2
        itr=self.head
        i=0
        while itr:
            #print(i,t)
            if(i==int(t)):
                return itr.data
            i+=1
            itr=itr.next

    def nth_node_from_end(self,n):
        t=self.get_length()-n
        itr=self.head
        i=0
        if(t<0):
            return -1
        while itr:
            if(i==t):
                return itr.data
            itr=itr.next
            i+=1

    def iter_reversal(self):
        prev,curr=None,self.head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        self.head=prev


    def dup_remove_sortedll(self):
        itr=self.head
        while itr.next:
            if(itr.data==itr.next.data):
                itr.next=itr.next.next
            else:
                itr=itr.next

    def recur_reverse(self,node=None,prev=None):
        if node is None:
            node=self.head
        if node is None:
            return
        nxt=node.next
        node.next=prev
        if nxt is None:
            self.head=node
        else:
            self.recur_reverse(nxt,node)

    def k_reversal_temp(self,k):
        curr,prev,count=self.head,None,0
        while(count<k):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
            count+=1
        self.head=prev


    def k_reversal(self,k):
        isFirstpass=True
        curr,prevfirst=self.head,None
        while(curr):
            first,prev=curr,None
            count=0
            while(curr!=None and count<k):
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
                count+=1
            if isFirstpass:
                self.head=prev
                isFirstpass=False
            else:
                prevfirst.next=prev
            prevfirst=first

    def detect_loop_dest(self):
        temp=Node(None,None)
        curr=self.head
        while curr:
            t=curr.next
            if(curr.next==temp):
                return True
            else:
                curr.next=temp
            curr=t
        return False

    def detect_loop_floyd(self):
        slow=self.head
        fast=self.head
        while slow:
            slow=slow.next
            if(fast.next==None):
                return False
            else:
                fast=fast.next.next
            if(slow==fast):
                return True
        return False






ll1=singly_LinkedList()
ll1.insert_values([8,12,14,55,87])

ll2=singly_LinkedList()
ll2.insert_values([3,4,89,777,929])

ll3=singly_LinkedList()
ll3.insert_values([12,44,45,66,89,98,1009])

def sortedMerge(head1, head2):
    if(head1.data>head2.data):
        head1,head2=head2,head1
    i=head1
    j=head2
    while(i!=None and j!=None):
        x=i.next
        y=j.next
        if(i.next==None):
            i.next=j
            if(j.next==None):
                break
            j=y
        if(i.next.data>j.data):
            i.next=j
            j.next=x
            j=y
        else:
            i=x
    return head1

    def mergeKLists(arr, K):
        if K == 0:
            return None
        if K == 1:
            return arr[0]

        mid = K // 2
        left = self.mergeKLists(arr[:mid], len(arr[:mid]))
        right = self.mergeKLists(arr[mid:], len(arr[mid:]))

        return sortedMerge(left, right)

print(mergeKLists([ll1.head,ll2.head,ll3.head]),3)



'''while curr.next:
    curr=curr.next
curr.next=ll2.head.next.next'''






















        












































            





























