arr=[1,2,3,4,5]
for start in range(len(arr)):
    for end in range(start,len(arr)):
        for x in range(start,end+1):
            print(arr[x],end=" ")
        print()
