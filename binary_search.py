arr=[1,2,3,4,5,6,7,8,9]
flag=False
key=2
low =0
high=len(arr)-1
mid=(low+high)//2
while low <=high and not flag:
    mid=(low+high)//2
    if key==arr[mid]:
        flag=True
        loc=mid
    elif key<arr[mid]:
        high=mid-1
    elif key>arr[mid]:
        low=mid+1
if flag==True:
    print("Search successfull and location is",loc)
else:
    print("Key not found")
