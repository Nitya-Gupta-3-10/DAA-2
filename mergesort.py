def mergesort(arr1,arr2,merge):
    i=0
    j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            merge.append(arr1[i])
            i=i+1
        else :
            merge.append(arr2[j])
            j=j+1
    while len(arr1)>i:
        merge.append(arr1[i])
        i=i+1
    while len(arr2)>j:
        merge.append(arr2[j])
        j=j+1


arr1=[1,3,5]
arr2=[2,4,6]
merge=[]
mergesort(arr1,arr2,merge)
print(merge)
