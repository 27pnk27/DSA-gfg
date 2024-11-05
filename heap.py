import heapq as hp #for minheap

'''Tree and array joint data structure
    Min_heap -> Every Node.data<Descendants.data
    Max_heap -> Every Node.data>Descendants.data
    Complete binary tree
    Node(arr[i]).left=Node(arr[2*i+1])
    Node(arr[i]).right=Node(arr[2*i+2])
    parent of Node(arr[i])=arr[(i-1)//2]'''

data=[10,20,43,1,2,65,17,44,2,3,1]

hp.heapify(data)
print(data)

hp.heappop(data)
print(data)

hp.heappush(data,2.5)
print(data)

class MaxHeap:
    def __init__(self):
        self.max_heap=[]
        self.size=0

    def push(self,data):
        self.max_heap.append(data)
        self.size+=1
        i=self.size-1
        while(i>0):
            if(self.max_heap[i]>self.max_heap[(i-1)//2]):
                self.max_heap[i],self.max_heap[(i-1)//2]=self.max_heap[(i-1)//2],self.max_heap[i]
                i=(i-1)//2
            else:
                break

    def heapify(self,a,n,i):
        largest=i
        left=2*i+1
        right=2*i+2

        if left < n and a[left] > a[largest]:
            largest = left

        # If the right child exists and is greater than the current largest
        if right < n and a[right] > a[largest]:
            largest = right

        # If the largest is not the root
        if largest != i:
            a[i], a[largest] = a[largest], a[i]  # Swap
            self.heapify(a, n, largest)

    def build_heap(self, a):
        self.max_heap = a[:]  # Copy the input array to self.max_heap
        self.size = len(a)
        n = self.size
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(self.max_heap, n, i)

    def pop(self):
        if self.size == 0:
            return None
        if self.size == 1:
            self.size -= 1
            return self.max_heap.pop()

        # Swap the root with the last element
        root = self.max_heap[0]
        self.max_heap[0] = self.max_heap.pop()  # Remove last element and place it at the root
        self.size -= 1

        # Restore the heap property starting from the root
        self.heapify(self.max_heap, self.size, 0)

        return root

    def delete(self,index):
        k=self.max_heap.pop(index)
        n=self.size
        self.heapify(self.max_heap,n,index)
        return k

    def heapify_tuple(self,a,n,i):
        largest=i
        left=2*i+1
        right=2*i+2

        if left < n and a[left][0] > a[largest][0]:
            largest = left

        # If the right child exists and is greater than the current largest
        if right < n and a[right][0] > a[largest][0]:
            largest = right

        # If the largest is not the root
        if largest != i:
            a[i], a[largest] = a[largest], a[i]  # Swap
            self.heapify_tuple(a, n, largest)

    def build_heap_tuple(self, a):
        self.max_heap = a[:]  # Copy the input array to self.max_heap
        self.size = len(a)
        n = self.size
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_tuple(self.max_heap, n, i)




k=MaxHeap()
k.build_heap([99,2,12,2314,7,5,3,1,9])
#print(k.max_heap)
#print(k.delete(4))
#print(k.max_heap,k.size)


'''If we want to sort in increasing order use Max Heap
    If we want to sort in decreasing order use Min Heap'''

def heap_sort(a):
    k=MaxHeap()
    k.build_heap(a)
    n=k.size
    for i in range(n-1,0,-1):
        k.max_heap[0],k.max_heap[i]=k.max_heap[i],k.max_heap[0]
        n-=1
        k.heapify(k.max_heap,n,0)

    return k.max_heap
k.build_heap([88,21,3,4,23,25,2,99,555])
#print(heap_sort(k.max_heap))

#print(heap_sort([99,32,2,88,3,1,4,51,9]))

def k_sort(a,k):
    n=len(a)
    for i in range(n):
        x = max(0, i - k)
        y = min(n, i + k + 1)
        sub = heap_sort(a[x:y])
        a[x:y]=sub

    return a

print('feq',k_sort([9,8,7,18,5,17],2))

def purchase_max(a,sum):

    res=0
    while(sum>0):
        hp.heapify(a)
        sum-=hp.heappop(a)
        res+=1
        if(sum<a[0]):
            break

    return res

#print(purchase_max([12,1,5,111,200],10))

def k_largest(a,k):
    n=len(a)
    b=a[:k]

    for i in range(k,n):
        if(b[0]<a[i]):
            hp.heapreplace(b,a[i])

    return b

#print(k_largest([5,15,10,20,8,25,18],3))



def k_smallest(a,k):
    n=len(a)
    b=a[:k]
    x=MaxHeap()
    x.build_heap(b)
    for i in range(k,n):
        #print(x.max_heap)
        if(x.max_heap[0]>a[i]):
            x.pop()
            x.push(a[i])

    return x.max_heap


print(k_smallest([5,15,10,20,8,25,18],3))

def k_closest(a,x,k):
    n=len(a)
    b=[]
    for i in range(n):
        b.append((abs(a[i]-x),i))

    c=b[:k]
    x=MaxHeap()
    x.build_heap_tuple(c)
    for i in range(k,n):
        if(x.max_heap[0][0]>b[i][0]):
            x.pop()
            x.push(b[i])
    f=[]
    for i in x.max_heap:
        f.append(a[i[1]])

    return f

print(k_closest([10,15,7,3,4],8,2))

def merge_k_sorted_arrays(a):
    k=len(a)
    x=[]
    for i in range(k):
        hp.heappush(x,(a[i][0],i,0))

    res=[]
    while x:

        temp=hp.heappop(x)
        res.append(temp[0])
        if temp[2] + 1 < len(a[temp[1]]):
            hp.heappush(x,(a[temp[1]][temp[2]+1],temp[1],temp[2]+1))

    return res

print(merge_k_sorted_arrays([[10,20],[5,15],[4,9,11]]))

def median_of_a_stream(a):
    n=len(a)
    left=MaxHeap()
    right=[]
    left.push(a[0])
    l=1
    r=0
    res=[a[0]]
    for i in range(1,n):
        if(l==r):
            if(a[i]>right[0]):
                temp=hp.heappop(right)
                left.push(temp)
                hp.heappush(right,a[i])
            else:
                left.push(a[i])
            l+=1
            res.append(left.max_heap[0])
        else:
            if(a[i]<left.max_heap[0]):
                temp=left.pop()
                hp.heappush(right,temp)
                left.push(a[i])
            else:
                hp.heappush(right,a[i])
            r+=1
            res.append((left.max_heap[0]+right[0])/2)

    return res

print(median_of_a_stream([25,7,10,15,20]))




































































































































































