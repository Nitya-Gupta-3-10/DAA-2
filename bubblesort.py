def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

if __name__=='__main__':
    arr=[41,2,45,4,1,24]
    bubblesort(arr)a
    print(arr)
