# Python 3.6

# check if two 1D lines overlap
# Invoke: isLinesOverlap((x1, x2), (x3, x4))
# where (x1, x2) is line 1, and (x3, x4) is line 2
# Return: True for overlap, False for otherwise
def isLinesOverlap(line1, line2):
    (x1, x2) = line1
    (x3, x4) = line2
	
    l1 = min(x1, x2)
    r1 = max(x1, x2)

    if x3 >= l1 and x3 <= r1:
        return True
    elif x4 >= l1 and x4 <= r1:
        return True
    return False

# test
print(isLinesOverlap((1, 5), (2, 6)))	# return True
print(isLinesOverlap((1, 5), (6, 8)))   # return False
