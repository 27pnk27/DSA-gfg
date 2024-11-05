def snake(a):
    n=len(a)
    m=len(a[0])
    s=[]
    for i in range(n):
        if(i%2==0):
            for j in range(m):
                s.append(a[i][j])
        else:
            for j in range(m-1,-1,-1):
                s.append(a[i][j])
    return s

print(snake([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))

def boundary(a):
    n=len(a)
    m=len(a[0])
    s=''
    if(m==1):
        for i in range(n):
            s+=str(a[i][0])+' '
    elif(n==1):
        for i in range(m):
            s+=str(a[0][i])+' '

    else:
        for i in range(m):
            s+=str(a[0][i])+' '
        for i in range(1,n-1):
            s+=str(a[i][m-1])+' '
        for i in range(m-1,-1,-1):
            s+=str(a[n-1][i])+' '
        for i in range(n-2,0,-1):
            s+=str(a[i][0])+' '
    return s

print(boundary([[1]]))

def transpose(a):
    n=len(a)
    for i in range(n):
        for j in range(i+1,n):
            a[i][j],a[j][i]=a[j][i],a[i][j]
    return a

print(transpose([[1,1],[2,2]]))

def ccw_rotation(a):
    a=transpose(a)
    a=a[::-1]
    return a

print(ccw_rotation([[1,2,3],[4,5,6],[7,8,9]]))

def spiral_traversal(a):
    n=len(a)
    m=len(a[0])
    s=''
    top,bottom,left,right=0,n-1,0,m-1
    while(top<=bottom and right>=left):
        for i in range(left,right+1):
            s+=str(a[top][i])+' '
        top+=1
        for i in range(top,bottom+1):
            s+=str(a[i][right])+' '
        right-=1
        for i in range(right,left-1,-1):
            s+=str(a[bottom][i])+' '
        bottom-=1
        for i in range(bottom,top-1,-1):
            s+=str(a[i][left])+' '
        left+=1
    return s

print(spiral_traversal([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))

def search_rc_sorted_matrix(a,x):
    n=len(a)
    m=len(a[0])
    i,j=0,m-1
    while(i<n and j>=0):
        if(a[i][j]==x):
            return i,j
        elif(a[i][j]>x):
            j-=1
        else:
            i+=1
    return -1


print(search_rc_sorted_matrix([[10,20,30,40],[15,25,35,45],[27,29,37,48],[32,33,39,50]],33))

def sorted_merge(a,b):
    n=len(a)
    m=len(b)
    i,j=0,0
    c=[]
    while(i<n and j<m):
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
    while(i<n):
        c.append(a[i])
        i+=1
    while(j<m):
        c.append(b[j])
        j+=1
    return c

def median_gfg_matrix(a):
    m=len(a[0])
    n=len(a)
    c=a[0]
    for i in range(1,n):
        c=sorted_merge(c,a[i])
    return c[int(m*n/2)]

print(median_gfg_matrix([[1,10,20],[15,25,30],[5,8,40]]))






































