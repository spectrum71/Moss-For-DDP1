def labxx_sort(list_to_sort):
	if len(list_to_sort) == 1:
		return list_to_sort
	if low < high:
		pi = partition(list_to_sort, low, high)

		quickSort(list_to_sort, low, pi-1)
		quickSort(list_to_sort, pi+1, high)
	
	return list_to_sort
	
def partition(list_to_sort, low, high):
	i = (low-1)
	pivot = list_to_sort[high]
 
	for j in range(low, high):
        if list_to_sort[j] <= pivot:

			i = i+1
			list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]
 
	list_to_sort[i+1], list_to_sort[high] = list_to_sort[high], list_to_sort[i+1]
    return (i+1)