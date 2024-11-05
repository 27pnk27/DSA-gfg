def isprime(n):
    if(n==1):
        raise IndexError('Neither prime nor composite')
    if(n==2 or n==3):
        return True
    if(n%2==0 or n%3==0):
        return False
    else:
        i=5
        while(i^2<n):
            if(n%i==0 or n%(i+2)==0):
                return False
        return True

def sieve_of_eratosthenes(n):
    prime=[True]*(n+1)
    p=2
    while(p*p<n):
        if(prime[p]==True):
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
    ans=''
    for i in range(2,n+1):
        if(prime[i]==True):
            ans+=str(i)+' '
    return ans





print(sieve_of_eratosthenes(111))

