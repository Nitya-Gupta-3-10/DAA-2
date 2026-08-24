arr=[1,2,3,4,5]
res=[]
for start in range(len(arr)):
    for end in range(start,len(arr)):
        sum=0
        for x in range(start,end+1):
            sum=sum+arr[x]
            res.append(sum)
print(res)
print(max(res))
