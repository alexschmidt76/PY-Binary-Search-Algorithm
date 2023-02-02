def binary_search(data, el):
    if len(data) == 0:
        return False
    mid = len(data) // 2
    if data[mid] == el:
        return True
    elif data[mid] < el:
        return binary_search(data[mid:], el)
    else:
        return binary_search(data[:mid], el)

test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31]

print(binary_search(test_list, 12))