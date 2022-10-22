from typing import List


def merge_sort(data) -> None:
    if len(data) > 1:
        mid = len(data) // 2
        l_arr = data[:mid]
        r_arr = data[mid:]
        merge_sort(l_arr)
        merge_sort(r_arr)

        data = merge(l_arr, r_arr, data)


def merge(l_arr, r_arr, arr):
    i = j = k = 0

    while j < len(l_arr) and k < len(r_arr):
        if l_arr[j] < r_arr[k]:
            arr[i] = l_arr[j]
            j += 1
        else:
            arr[i] = r_arr[k]
            k += 1
        i += 1

    while j < len(l_arr):
        arr[i] = l_arr[j]
        i += 1
        j += 1

    while k < len(r_arr):
        arr[i] = r_arr[k]
        i += 1
        k += 1

    return arr


# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
    if item.isnumeric():
        data.append(int(item))
    elif item.lstrip("-").isnumeric():
        data.append(int(item))
merge_sort(data)
print(data)
