
# T R Y  E V E R Y T H I N G
import Queue

def swap(lst, i, j):
    sublst = lst[i:j+1]
    sublst.reverse()
    lst = lst[:i] + sublst + lst[j+1:]
    return lst

def reversalDistance(s, t):
	queue = Queue.Queue()
	visited = set()

	queue.put((s,0))
	while not queue.empty():
		x,d = queue.get()
		visited.add(tuple(x))
		if x == t:
			return d
		for i in xrange(len(x)):
			for j in xrange(i+1, len(x)):
				tmp = swap(x[:], i, j)
				if tuple(tmp) not in visited:
					queue.put((tmp, d+1))


with open("dataset.txt", "r") as f:
	content = f.readlines()

reversalDistance([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [3, 1, 5, 2, 7, 4, 9, 6, 10, 8])

"""
nums = []
for c in content:
	numbers = list(map(int, c.split()))
	if numbers:
		nums.append(numbers)

for i in range(0, len(nums),2):
	print reversalDistance(nums[i], nums[i+1])
"""