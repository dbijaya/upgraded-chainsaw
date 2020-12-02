import statistics as st

n = int(input())
darr = [int(k) for k in input().split()]
farr = [int(k) for k in input().split()]
N = sum(farr)

data_set = sorted(list(zip(darr, farr)))
data = []
for m,n in data_set:
    data.extend([m for i in range(n)])

if n%2==0:
    q1 = st.median(data[:N//2])
    q3 = st.median(data[N//2:])
else:
    q1 = float(st.median(data[:N//2]))
    q3 = float(st.median(data[N//2+1:]))
ir = round(float(q3-q1), 1)
print(ir)