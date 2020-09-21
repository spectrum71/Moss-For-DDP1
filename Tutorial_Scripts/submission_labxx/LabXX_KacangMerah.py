def labxx_sort(list_to_sort):
	gap = len(list_to_sort) // 2
	while gap > 0:

		for i in range(gap, len(list_to_sort)):
			temp = list_to_sort[i]
			j = i
			
			while j >= gap and list_to_sort[j - gap] > temp:
				list_to_sort[j] = list_to_sort[j - gap]
				j = j-gap
			list_to_sort[j] = temp

		gap = gap//2
	
	return list_to_sort