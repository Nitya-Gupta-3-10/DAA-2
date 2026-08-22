def pivot_place(list1,first,last):
	pivot=list1[first]
	left=first+1;
	right=last
	while True:
		while left<=right and list1[left]<=pivot:
			left=left+1
		while left<=right and list1[right]>=pivot:
			right=right-1
		if right<left:
			break;
		else:
			list1[left],list1[right]=list1[right],list1[left]
	list1[first],list1[right]=list1[right],list1[first]
	return right

def quickSort(list1,first,last):
	if first<last:
		p=pivot_place(list1,first,last)
		quickSort(list1,first,p-1)
		quickSort(list1,p+1,last)

if __name__ == '__main__':
	l1=[45,3,8,56,2,11,29,13]
	quickSort(l1,0,len(l1)-1)
	print(l1)
