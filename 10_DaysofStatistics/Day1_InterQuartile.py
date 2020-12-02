# The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e.,Q3-Q1).
# Given an array,X,of n integers and an array,F,representing the respective frequencies of X's elements, construct a data set,S,
# where each xi occurs at frequency fi. Then calculate and print S's interquartile range, rounded to a scale of 1 decimal place.


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

n = int(input())
darr = [int(k) for k in input().split()]
farr = [int(k) for k in input().split()]

data_set = sorted(list(zip(darr, farr)))
data = []
for m,n in data_set:
    data.extend([m for i in range(n)])


array = divideArray(data)
q1 = calculateQuartile(array[0])
q3 = calculateQuartile(array[1])

# inter_quartile = round(q3 - q1)
print(round((q3-q1), 1))
