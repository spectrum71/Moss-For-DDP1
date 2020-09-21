def labxx_sort(list_to_sort):
	for iter_num in range(len(list_to_sort)-1,0,-1):
		for idx in range(iter_num):
			if list_to_sort[idx]>list_to_sort[idx+1]:
				list_to_sort[idx], list_to_sort[idx+1] = list_to_sort[idx+1], list_to_sort[idx]
	
	return list_to_sort