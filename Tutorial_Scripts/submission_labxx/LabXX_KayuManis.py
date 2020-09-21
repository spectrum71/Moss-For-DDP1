def labxx_sort(list_to_sort):
	if len(list_to_sort) <= 1:
		return list_to_sort

	middle = len(list_to_sort) // 2
	left_list = list_to_sort[:middle]
	right_list = list_to_sort[middle:]

	left_list = labxx_sort(left_list)
	right_list = labxx_sort(right_list)
	return list(merge(left_list, right_list))

def merge(left_half,right_half):

	res = []
	while len(left_half) != 0 and len(right_half) != 0:
		if left_half[0] < right_half[0]:
			res.append(left_half[0])
			left_half.remove(left_half[0])
		else:
			res.append(right_half[0])
			right_half.remove(right_half[0])
	if len(left_half) == 0:
		res = res + right_half
	else:
		res = res + left_half
	return res