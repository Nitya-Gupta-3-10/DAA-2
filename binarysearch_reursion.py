def binarysearch(arr,low,high,key):
    if low>high:
        return -1
    mid=(low+high)//2
    if key==arr[mid]:
        return mid
    elif key<arr[mid]:
        return binarysearch(arr,low,mid-1,key)
    elif key>arr[mid]:
        return binarysearch(arr,mid+1,high,key)

if __name__ == '__main__':
    arr=[11,22,33,44,55,66,77,88,99]
    low=0
    high=len(arr)-1
    key=88
    loc=binarysearch(arr,low,high,key)
    print(loc)
   

   
