# returns index of search element if exists, otherwise return index of greatest element less than
def bin_search(arr, search):
	start = 0
	end = len(arr) - 1
	while True:
		if (start > end):
			return start
		mid = (end + start) // 2
		if (search == arr[mid]):
			return mid
		elif (search > arr[mid]):
			start = mid + 1
		elif (search < arr[mid]):
			end = mid - 1
			
n = int(input())
lines = []
y_coords = input().split()
for coord in y_coords:
	lines.append(int(coord))
lines.sort()
q = int(input())
for i in range(q):
	coords = input().split()
	x = int(coords[0])
	y = int(coords[1])
	y_int = x + y
	print(bin_search(lines, y_int))
