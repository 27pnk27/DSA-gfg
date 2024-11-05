def activity_selection(a):
    n=len(a)
    for i in range(1,n):
        j=i
        while(a[j][1]<a[j-1][1] and j>0):
            a[j],a[j-1]=a[j-1],a[j]
            j-=1

    curr=a[0]
    ans=1
    for i in range(1,n):
        if(curr[1]<=a[i][0]):
            curr=a[i]
            ans+=1
    return ans

#print(activity_selection([[1,3],[2,4],[3,8],[10,11]]))

def frac_knapsack_prob(a,k):
    n=len(a)
    sum=0
    for i in a:
        sum+=i[0]
    if(sum<k):
        p=0
        for i in a:
            p+=i[1]
        return p
    for i in range(1,n):
        j=i
        while((a[j][1]/a[j][0])<(a[j-1][1]/a[j-1][0]) and j>0):
            a[j],a[j-1]=a[j-1],a[j]
            j-=1
    a=a[::-1]
    i=0
    ans=0
    while(k>a[i][0]):
        ans+=a[i][1]
        k-=a[i][0]
        i+=1
    ans+=(a[i][1]*(k)/a[i][0])
    return int(ans)



print(frac_knapsack_prob([[10,200],[5,50],[20,100]],70))









