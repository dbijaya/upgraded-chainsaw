# Given an array,X,of N integers, calculate and print the standard deviation.
# Your answer should be in decimal form, rounded to a scale of 1 decimal place (i.e.,12.3format).
# An error margin of +-0.1 will be tolerated for the standard deviation.

import math

n = int(input())
arr = [int(k) for k in input().split()]

mean = round(sum(arr)/n, 1)

sq_distance = math.sqrt((sum(list(map(lambda i: pow((i-mean), 2), arr))))/n)

# std_dev = math.sqrt(sq_distance/n)
# print(round(std_dev, 1))

print(round(sq_distance, 1))
