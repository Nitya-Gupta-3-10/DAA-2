arr=[1,2,3,4,5]
maxsum=0
currsum=0
for start in range(0,len(arr)):
    currsum+=arr[start]
    maxsum=max(currsum,maxsum)
    if currsum<0:
        currsum=0
print("max sum",maxsum)
