# Given an array,X,of N integers and an array,W, representing the respective weights of X's elements,
# calculate and print the weighted mean of X's elements. Your answer should be rounded to a scale of 1 decimal place (i.e.,12.3 format).

n = int(input())
warr = [int(x) for x in input().split()]
arr = [int(y) for y in input().split()]

index = [x for x in range(0,n)]
# up = sum(list(map(lambda x: (arr[x]*warr[x]), index])))
up = sum(list(map(lambda t: (arr[t]*warr[t]),index)))
down = sum(arr)

print(round((up/down),1))