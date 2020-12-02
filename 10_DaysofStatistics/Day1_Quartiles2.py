def calculateQuartile(arr):
    n = len(arr)
    if n%2==0:
        q = (arr[n//2]+arr[-(n//2+1)])/2
    else:
        q =arr[n//2]
    return q

def divideArray(arr):
    n = len(arr)
    if n%2==0:
        arr1 = arr[0:(n//2)]
        arr2 = arr[(n//2):(n+1)]
    else:
        arr1 = arr[0:(n//2)]
        arr2 = arr[(n//2+1):(n+1)]
    return arr1, arr2

b = int(input())
arr = sorted([int(k) for k in input().split()])
q2 = calculateQuartile(arr)

array = divideArray(arr)
q1 = calculateQuartile(array[0])
q3 = calculateQuartile(array[1])

# q1 = int(map(calculateQuartile, divideArray(arr)[0]))
# q3 = int(map(calculateQuartile, divideArray(arr)[1]))

print(int(q1))
print(int(q2))
print(int(q3))
