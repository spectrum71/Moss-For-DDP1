def labxx_sort(list_to_sort):
	for i in range(1, len(list_to_sort)):
		j = i-1
		nxt_element = list_to_sort[i]
		
		while (list_to_sort[j] > nxt_element) and (j >= 0):
			list_to_sort[j+1] = list_to_sort[j]
			j=j-1
		list_to_sort[j+1] = nxt_element
	
	return list_to_sort