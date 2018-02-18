
__author__ = 'J.R.'


def max_subarray(a):
    if a is None or len(a) == 0:
        return 0

    n = len(a)
    d = [0] * n
    d[0] = a[0]
    max_sum = d[0]
    for i in range(1, n):
        d[i] = a[i] + (0 if d[i-1] < 0 else d[i-1])
        max_sum = max(max_sum, d[i])
    return max_sum


def max_product_subarray(a):
    if a is None or len(a) == 0:
        return 0

    n = len(a)
    result = a[0]
    imax = result
    imin = result
    for i in range(1, n):
        if a[i] < 0:
            c = imax
            imax = imin
            imin = imax
        imin = min(a[i], a[i]*imin);
        imax = max(a[i], a[i]*imax);
        result = max(result, imax)
    return result


def product_except_self(a):
    if a is None or len(a) == 0:
        return 0

    n = len(a)
    r = [0] * n
    r[0] = 1
    for i in range(1, n):
        r[i] = r[i-1]*a[i-1]
    s = 1
    for i in range(n-1, -1, -1):
        r[i] *= s
        s = s * a[i]
    return r


def max_subarray_sum_equals_k(a, k):
    if a is None or len(a) == 0:
        return 0

    n = len(a)
    total_sum = 0
    max_len = 0
    d_sum = {}
    for i in range(n):
        total_sum = total_sum + a[i]
        if sum == k:
            max_len = i + 1
        elif (total_sum - k) in d_sum:
            max_len = max(max_len, i - d_sum[total_sum - k])
        if sum not in d_sum:
            d_sum[total_sum] = i
    return max_len

if __name__ == '__main__':

    aa = [1, 3, -4, 0, 8, 1, 2, 3, -10, 20]
    print('Max sum is {} '.format(max_subarray(aa)))

    aa = [1, 2, -2, -4, 1, 0, 10]
    print('Max product is {} '.format(max_product_subarray(aa)))

    aa = [1, 2, 3, 4]
    print('Product every element to other elements except self {} '.format(product_except_self(aa)))

    aa = [1, 2, 3, 0, 0, 0, 0, 2, 0, 0, 4]
    print('Longest sub-array which sum equals {} is of size {} '.format(7, max_subarray_sum_equals_k(aa, 7)))
