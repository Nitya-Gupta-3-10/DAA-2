arr=[1,2,3,4,5]
maxsum=0
res=[]
for start in range(0,len(arr)):
    currsum=0
    for end in range(start,len(arr)):
        currsum+=arr[end]
        maxsum=max(currsum,maxsum)
print("max sum",maxsum)
