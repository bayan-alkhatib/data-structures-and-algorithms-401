def merge_sort(arr):
    n = len(arr) 

    if n > 1:
      mid = n//2
      left = arr[:mid]
      right = arr[mid:]
      merge_sort(left)
      merge_sort(right)
      merge(left,right, arr)

    return arr


def merge(left, right, arr):
    l_idx = 0
    r_idx = 0
    arr_idx = 0

    while l_idx < len(left) and r_idx < len(right):

        if left[l_idx] <= right[r_idx]:
            arr[arr_idx] = left[l_idx]
            l_idx += 1

        else:
            arr[arr_idx] = right[r_idx]
            r_idx += 1

        arr_idx = arr_idx + 1

    if l_idx == len(left):
       for item in right[r_idx:]:
            arr[arr_idx] = item
            arr_idx += 1
    else:
       for item in left[l_idx:]:
            arr[arr_idx] = item
            arr_idx += 1

