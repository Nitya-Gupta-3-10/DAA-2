def fractknapsack(items,capacity):
    max_val=0
    items.sort(key= lambda x:x[0]//x[1],reverse=True)
    knapsack=0.0
    for val,wt in items:
        if wt<=capacity:
            capacity-=wt
            max_val=max_val+val
        else:
            max_val+=(val/wt)*capacity
            break
    return max_val
if __name__ == '__main__':
    items=[[150,15],[60,10],[100,20],[120,30],[80,40]]
    capacity=60
    res=fractknapsack(items,capacity)
    print(res)
