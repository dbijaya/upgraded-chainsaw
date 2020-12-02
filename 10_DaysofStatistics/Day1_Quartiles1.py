#  Given an array,X, of N integers, calculate the respective first quartile (Q1), second quartile (Q2), and third quartile (Q3).
# It is guaranteed that Q1, Q2, and Q3 are integers.

n = int(input())
arr = sorted([int(k) for k in input().split()])
q1, q2, q3 = 0, 0, 0
if n%2==0:
    q2 = (arr[n//2]+arr[-(n//2+1)])/2
    
    arr1 = arr[0:(n//2)]
    arr2 = arr[(n//2):(n+1)]
    
    m=len(arr1)
    if m%2==0:
        q1 = (arr1[m//2]+arr1[-(m//2+1)])/2
        q3 = (arr2[m//2]+arr2[-(m//2+1)])/2        
    else:
        q1 =arr1[m//2]
        q3 =arr2[m//2]
        
else:
    q2 =arr[n//2]
    
    arr1 = arr[0:(n//2)]
    arr2 = arr[(n//2+1):(n+1)]
    
    m=len(arr1)
    if m%2==0:
        q1 = (arr1[m//2]+arr1[-(m//2+1)])/2
        q3 = (arr2[m//2]+arr2[-(m//2+1)])/2        
    else:
        q1 =arr1[m//2]
        q3 =arr2[m//2]

print(int(q1))
print(int(q2))
print(int(q3))