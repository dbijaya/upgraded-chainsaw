#  Task:  Given an array,X,of N integers, calculate and print the respective mean, median, and mode on separate lines.
# If your array contains more than one modal value, choose the numerically smallest one.

# Note: Other than the modal value (which will always be an integer),
# your answers should be in decimal form, rounded to a scale of 1 decimal place (i.e.,12.3, 7.0 format).


# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
# arr = list(input().split())
arr = [int(x) for x in input().split()]

if n>=10 & n<=2500:
        
    # sums = 0
    # for i in arr:
    #     sums+=int(i)
    sums = sum(arr)/n
    print(round(sums, 1))

    sort_arr = sorted([int(x) for x in arr])
    # mid=int(n/2)
    # med = (sort_arr[mid]+sort_arr[mid-1])/2
    med=0
    for m in sort_arr:
        if m<0 | m>=(pow(10,5)):
            print('Invalid Data.')
            break
    med = (sort_arr[n//2]+sort_arr[(n//2)-1])/2
    print(round(med, 1))

    # freq = []
    # for val in sort_arr:
    #     freq.append(sort_arr.count(val))
    freq = {x:sort_arr.count(x) for x in sort_arr}

    x = min(sorted(list(freq.values())))
    mode = [k for k,v in freq.items() if v==x][0]
    print(mode)
    
else:
    print('Invalid Data.')
