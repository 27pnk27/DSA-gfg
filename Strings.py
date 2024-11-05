def ispalin(a):
    if(a==a[::-1]):
        return 'Yes'
    else:
        return 'No'

print(ispalin('kaak'))

def iter_subsequence(a, b):
    m = len(b)
    n = len(a)
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] == b[j]:
            j += 1
        i += 1
    return j == m

print(iter_subsequence('ABVD', 'AB'))
print(iter_subsequence('ABVD', 'ADB'))
print(iter_subsequence('ABVD', 'BVD'))
print(iter_subsequence('ABVD', 'BDA'))

def leftmost_repeating(a):
    n=len(a)
    for i in range(n):
        for j in range(i+1,n):
            if(a[j]==a[i]):
                return a[i]
                break
    return -1

print(leftmost_repeating('abbcb'))







