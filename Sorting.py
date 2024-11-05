def bubble_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(n-i-1):
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
        #print(a)
    return a

def select_sort(a):
    n=len(a)
    for i in range(n):

        res=float('inf')
        for j in range(i+1,n):
            if(a[j]<res):
                res=a[j]
                t=j
        a[t],a[i]=a[i],a[t]
    return a

def insert_sort(a):
    n=len(a)
    for i in range(1,n):
        j=i
        while(a[j]<a[j-1] and j>0):
            a[j],a[j-1]=a[j-1],a[j]
            j-=1
    return a

def sorted_merge(a,b):
    m=len(a)
    n=len(b)
    c=[]
    j=0
    i=0
    while(i<m and j<n):
        if(a[i]>=b[j]):
            c.append(b[j])
            j+=1
        else:
            c.append(a[i])
            i+=1
    while(j<n):
        c.append(b[j])
        j+=1
    while(i<m):
        c.append(a[i])
        i+=1
    return c

def merge(a,low,mid,high):
    left=a[low:mid+1]
    right=a[mid+1:high+1]
    i=0
    j=0
    k=low
    while(i<len(left) and j<len(right)):
        if(left[i]<=right[j]):
            a[k]=left[i]
            i+=1
            k+=1
        else:
            a[k] = right[j]
            j += 1
            k += 1
    while(i<len(left)):
        a[k] = left[i]
        i += 1
        k += 1
    while(j<len(right)):
        a[k] = right[j]
        j += 1
        k += 1
#print(merge([1,2,3,3,4,3,5,6,7],0,4,8))

def merge_sort(a,l,r):
    if(r>l):
        m=int((l+r)/2)
        merge_sort(a,l,m)
        merge_sort(a,m+1,r)
        merge(a,l,m,r)

x=[1,2,3,3,4,4,4,5,5,5,2,2,3,3,3]
merge_sort(x,0,14)
#print(x)

def sorted_intersect(a,b):
    i=0
    j=0
    n=len(a)
    m=len(b)
    c=[]
    while(i<n and j<m):
        if(a[i]==a[i-1] and i>0):
            i+=1
            continue
        if(a[i]==b[j]):
            c.append(a[i])
            i+=1
            j+=1
        elif(a[i]>b[j]):
            j+=1
        else:
            i+=1
    return c

#print(sorted_intersect([3,5,10,10,10,15,15,20],[5,10,10,15,30]))

def sorted_union(a,b):
    c=[]
    m=len(a)
    n=len(b)
    i=0
    j=0
    while(i<m and j<n):
        if(a[i]==a[i-1] and i>0):
            i+=1
            continue
        if(a[i]<b[j]):
            c.append(a[i])
            i+=1
        elif(a[i]>b[j]):
            c.append(b[j])
            j += 1
        else:
            c.append(a[i])
            i+=1
            j+=1
    while (i < m):
        if(a[i]==a[i-1] and i>0):
            i+=1
            continue
        c.append(a[i])
        i+=1
    while (j < n):
        if (b[j] == b[j - 1] and j > 0):
            j += 1
            continue
        c.append(b[j])
        j += 1
    return c

#print(sorted_union([2,3,3,3,4,4],[4,4]))

def count_and_merge(a,l,m,r):
    left=a[l:m+1]
    right=a[m+1:r+1]
    i=0
    j=0
    k=l
    c=0
    while(i<m-l+1 and j<r-m):
        if(left[i]<=right[j]):
            a[k]=left[i]
            i+=1
        else:
            a[k]=right[j]
            j+=1
            c+=m-l+1-i
        k+=1
    while(i<m-l+1):
        a[k] = left[i]
        i += 1
        k+=1
    while(j<r-m):
        a[k] = right[j]
        j += 1
        k+=1
    return c

#print(count_and_merge([2,5,8,11,3,6,9,13],0,3,7))

def count_invert(a,l,r):
    res=0
    if(r>l):
        m=int((l+r)/2)
        res+=count_invert(a,l,m)
        res+=count_invert(a,m+1,r)
        res+=count_and_merge(a,l,m,r)
    return res

def partition(a,ind):
    n=len(a)
    b=0
    left=[]
    right=[]
    for i in range(n):
        if(a[i]<=a[ind]):
            left.append(a[i])
        else:
            right.append(a[i])
    a=left+right
    return a

def lomuto_partition(a,l,h):
    pivot=a[h]
    i=l-1
    for j in range(l,h):
        if(a[j]<pivot):
            i+=1
            a[i],a[j]=a[j],a[i]
    a[h],a[i+1]=a[i+1],a[h]
    return i+1

#print(lomuto_partition([3,8,6,12,10,7],0,3))

def hoare_partition(a, l, h):
    pivot = a[l]
    i = l
    j = h

    while j > i:
        # Increment i while a[i] is less than the pivot
        while a[i] < pivot:
            i += 1

        # Decrement j while a[j] is greater than the pivot
        while a[j] > pivot:
            j -= 1

        # If two indices crossed, break the loop
        if j <= i:
            break

        a[i], a[j] = a[j], a[i]
        print(i, j, a)

    return a,j
print(hoare_partition([11,8,6,12,10,7,9],0,6))

def lomuto_qsort(a,l,h):
    if(l<h):
        p=lomuto_partition(a,l,h)
        lomuto_qsort(a,l,p-1)
        lomuto_qsort(a,p+1,h)

t=[3,2,4,1,7,6,9]
lomuto_qsort(t,0,6)
print(t)

























































































