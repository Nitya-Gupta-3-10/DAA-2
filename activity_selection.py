def activity_selection(activities):
    activities.sort(key=lambda x:x[1])
    selected=[]
    selected.append(activities[0])
    last_finish=activities[0][1]
    for i in range(1,len(activities)):
        start=activities[i][0]
        finish=activities[i][1]
        if start >=last_finish:
            selected.append(activities[i])
        if start>= last_finish:
            selected.append(activities[i])
            last_finish=finish
    return selected

if __name__ == '__main__':
    activities=[(1,2),(3,4),(0,6),(5,7),(8,9),(5,9),(6,10),(8,11),(12,14),(13,15)]
    res=activity_selection(activities)
    print("Selected activities:")
    for activity in res:
        print(activity)
    print("Maximum number of activities=",len(res))
