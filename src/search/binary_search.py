

# find min elements in rotated sorted array
def find_min(a):

    if a is None or len(a) == 0:
        return None

    lo = 0
    hi = len(a) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if a[mid] < a[hi]:
            hi = mid
        else:
            lo = mid + 1
    return a[lo]


# find element in sorted array
def search(a, k):

    if a is None or len(a) == 0:
        return - 1

    lo = 0
    hi = len(a) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if a[mid] == k:
            return mid
        if k < a[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


# find element in rotated sorted array
def search_in_rotated_array(a, k):

    if a is None or len(a) == 0 or (len(a) == 1 and a[0] != k):
        return -1
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] == k:
            return mid
        if a[lo] <= a[mid]:
            if a[lo] <= k <= a[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if a[mid] <= k <= a[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return lo if a[lo] == k else -1


if __name__ == "__main__":
    aa = [6, 7, 1, 2, 3, 4, 5]
    v = 2
    result = search_in_rotated_array(aa, v)
    print('Index of {} in array is {}'.format(v, result))

    aa = [1]
    v = 1
    result = search_in_rotated_array(aa, v)
    print('Index of {} in array is {}'.format(v, result))

    aa = [3, 1]
    v = 1
    result = search_in_rotated_array(aa, v)
    print('Index of {} in array is {}'.format(v, result))

    aa = [1, 2, 3, 4, 5]
    v = 3
    result = search(aa, v)
    print('Index of {} in array is {}'.format(v, result))

    aa = [6, 7, 1, 2, 3, 4, 5]
    result = find_min(aa)
    print('Min element is {}'.format(result))