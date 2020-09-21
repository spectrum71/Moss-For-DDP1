def labxx_sort(list_to_sort):
	idx = 0
	while idx < n: 
		if idx == 0: 
			idx = idx + 1
		if list_to_sort[idx] >= list_to_sort[idx - 1]: 
			idx = idx + 1
		else: 
			list_to_sort[idx], list_to_sort[idx-1] = list_to_sort[idx-1], list_to_sort[idx] 
			idx = idx - 1
	
	return list_to_sort