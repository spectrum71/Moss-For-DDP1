def labxx_sort(list_to_sort):
	for idx in range(len(list_to_sort)):

		min_idx = idx
		for j in range( idx +1, len(list_to_sort):
			if list_to_sort[min_idx] > list_to_sort[j]:
				min_idx = j

		list_to_sort[idx], list_to_sort[min_idx] = list_to_sort[min_idx], list_to_sort[idx]
	
	return list_to_sort