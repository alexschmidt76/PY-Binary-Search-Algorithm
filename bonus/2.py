def binary_search(data, el):
    first = 0
    last = len(data) - 1
    found = False
    idx = int
    while not found and first <= last:
        mid = (first + last) // 2
        if data[mid] == el:
            found = True
        elif data[mid] > el:
            last = mid - 1
        else:
            first = mid + 1
    if found:
        return mid
    return -1

test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31]

print(binary_search(test_list, 12))