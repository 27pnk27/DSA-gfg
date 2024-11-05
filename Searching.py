def iter_binsearch(x,a,high,low):
    while(high>=low):
        mid=int((high+low)/2)
        if(x==a[mid]):
            return mid
        elif(x>a[mid]):
            low=mid+1
        else:
            high=mid-1
    return -1

#print(iter_binsearch(17,[7,12,17,22,55,75]))

def recur_binsearch(x,a,high,low):
    if(low>high):
        return -1
    mid=int((high+low)/2)
    if(a[mid]==x):
        return mid
    elif(a[mid]>x):
        return recur_binsearch(x,a,mid-1,low)
    else:
        return recur_binsearch(x,a,high,mid+1)

#print(recur_binsearch(22,[7,12,17,22,55,75],5,0))

def recur_first_occur(x,a,high,low):
    t=recur_binsearch(x,a,high,low)
    if(t==-1):
        return -1
    else:
        if(recur_binsearch(x,a,t-1,low)==-1):
            return t
        else:
            return recur_first_occur(x,a,t-1,low)

def iter_first_occur(x,a,high,low):

    while(high>=low):
        mid = int((high + low) / 2)
        if(a[mid]>x):
            high=mid-1
        elif(a[mid]<x):
            low=mid+1
        else:
            if(mid==0 or a[mid-1]!=a[mid]):
                return mid
            else:
                high=mid-1
    return -1

def iter_last_occur(x,a,high,low):
    while (high>=low):
        mid=int((high + low)/2)
        if(a[mid]>x):
            high=mid-1
        elif(a[mid]<x):
            low=mid+1
        else:
            if(mid==len(a)-1 or a[mid+1]!=a[mid]):
                return mid
            else:
                low=mid+1
    return -1

def iter_count(x,a,high,low):
    if(iter_first_occur(x,a,high,low)==-1):
        return 0
    else:
        q=iter_last_occur(x,a,high,low)
        b=iter_first_occur(x,a,high,low)
        return q-b+1

def iter_bin_count(a):
    n=len(a)
    y=iter_first_occur(1,a,n-1,0)
    return n-y

def sqrt(x):
    l=[]
    for i in range(1,x+1):
        l.append(i)
    high=x-1
    low=0
    while(high>=low):
        mid=int((high+low)/2)
        if(mid**2<=x<(mid+1)**2):
            return mid
        elif(x>=(mid+1)**2):
            low=mid+1
        else:
            high=mid-1

def infi_arr_search(x,a):
    i=1
    while(a[i]<x):
        i*=2
    if(x==a[i]):
        return i
    else:
        iter_binsearch(x,a,i-1,int(i/2)+1)

def rot_sort_search(x,a,high,low):             #Revisit
    while(high>=low):                          #Problem when reverse sorted grp given
        mid=int((high+low)/2)
        if(a[mid]>a[low]):
            c=iter_binsearch(x,a,mid,low)
            if(c!=-1):
                return c
            else:
                low=mid+1
        else:
            c = iter_binsearch(x,a,high,mid)
            if (c != -1):
                return c
            else:
                 high=mid-1
    return -1
#print(rot_sort_search(40,[5,8,10,20,40,60],5,0))

def peak_elements(a):
    high=len(a)-1
    low=0
    while(high>=low):
        mid=int((high+low)/2)
        if((mid==0 or a[mid-1]<=a[mid]) and (mid==len(a)-1 or a[mid]>=a[mid+1])):
            return mid
        elif(a[mid-1]<=a[mid]<=a[mid+1] and mid>0 and mid<len(a)-1):
            low=mid+1
        else:
            high=mid-1

def pair_sum(x,a):
    n=len(a)
    j=n-1
    i=0
    while(j>i):
        if(a[i]+a[j]==x):
            return True,i,j
        elif(a[i]+a[j]>x):
            j-=1
        else:
            i+=1
    return False

def triplet_sum(x,a):
    n=len(a)
    j=n-1
    i=0
    while(j>i):
        if(a[i]+a[j]<=x):
            if(iter_binsearch(x-a[i]-a[j],a,j-1,i+1)==-1):
                i+=1
            else:
                return True
        else:
            j-=1
    return False

def repeater(a):
    n=len(a)
    b=[0]*n
    for i in a:
        if(b[i]==0):
            b[i]=1
        else:
            return i

def cuts(a,mid):
    n=0
    i=0
    m=len(a)
    while(i<m-1):
        t=0
        while(t+a[i]<=mid):
            t+=a[i]
            if(i<m-1):
                i+=1
            else:
                if(t+a[i]>mid):
                    return n
                else:
                    return n
        n+=1
        #print(i,n,m,t)
    return n

def pages(a,k):
    high=sum(a)
    low=max(a)
    while(high>=low):
        mid=int((high+low)/2)
        if(cuts(a,mid)+1>k):
            low=mid+1
        elif(cuts(a,mid)+1<=k):
            high=mid-1
    return mid

print(pages([10,20,10,30],2))




















































































































































