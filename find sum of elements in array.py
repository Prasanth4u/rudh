sum=0
n=int(input())
a=list(map(int,input().strip().split()))[:n]
for i in range(0,len(a)):
    sum=sum+a[i]
print(sum)
