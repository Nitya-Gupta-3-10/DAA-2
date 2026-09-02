def mergesort(list):
    if len(list)>1:
        mid=len(list)//2
        list1=list[:mid]
        list2=list[mid:]
        mergesort(list1)
        mergesort(list2)
        i=j=k=0
        while i<len(list1) and j<len(list2):
            if list1[i]<list2[j]:
                list[k]=list1[i]
                i=i+1
                k=k+1
            else :
                list[k]=list2[j]
                j=j+1
                k=k+1
        while len(list1)>i:
            list[k]=list1[i]
            i=i+1
        while len(list2)>j:
            list[k]=list2[j]
            j=j+1
            

if __name__ == '__main__':
    list=[1,7,12,3,6,2,9]
    mergesort(list)
    print(list)
