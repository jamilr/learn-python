import math

__author__ = 'J.R.'


# find min value in a given array
def min_value(a):

    if a is None or len(a) == 0:
        return None

    n = len(a)
    min_val = a[0]
    for i in range(1, n):
        if a[i] < min_val:
            min_val = a[i]
    return min_val


# find max value in a given array
def max_value(a):

    if a is None or len(a) == 0:
        return None

    n = len(a)
    max_val = a[0]
    for i in range(1, n):
        if a[i] > max_val:
            max_val = a[i]
    return max_val


# find mode value in a given array
def mode_value(a):

    if a is None or len(a) == 0:
        return None

    freq_dict = {}
    n = len(a)
    mode_val = a[0]
    for i in range(1, n):
        if a[i] in freq_dict:
            freq_dict[a[i]] = freq_dict[a[i]] + 1
        else:
            freq_dict[a[i]] = 1

    mode_val = a[0]
    mode_freq = 1
    for key in freq_dict:
        if freq_dict[key] > mode_freq:
            mode_freq = freq_dict[key]
            mode_val = key

    return mode_val


# find mean value in a given array
def mean_value(a):

    if a is None or len(a) == 0:
        return None

    n = len(a)

    mean_val = 0
    for i in range(n):
        mean_val += a[i]

    return mean_val / n


# find median value in a given array
def median_value(a):

    if a is None or len(a) == 0:
        return None

    n = len(a)
    if n % 2 == 0:
        return (a[n//2] + a[n//2 + 1]) // 2
    else:
        return a[n//2]


# find sample variance from the given array of data points
def sample_variance(a):

    if a is None or len(a) == 0:
        return 0

    n = len(a)
    total_sum = 0
    diff_val = 0
    mean_val = mean_value(a)
    for i in range(n):
        diff_val = (a[i] - mean_val)
        diff_val = diff_val ** 2
        total_sum += diff_val
    return total_sum / (n - 1)


# find sample standard deviation from the given array of data points
def sample_std_dev(a):

    if a is None or len(a) == 0:
        return 0

    variance = sample_variance(a)
    return math.sqrt(variance)


if __name__ == '__main__':

    aa = [1, 2, 3, 1, 2, 3, 1, 0, 2]
    print('Mode value is {}'.format(mode_value(aa)))
    print('Mean value is {}'.format(mean_value(aa)))
    print('Median value is {}'.format(median_value(aa)))
    print('Max value is {}'.format(max_value(aa)))
    print('Min value is {}'.format(min_value(aa)))
    print('Variance value is {}'.format(sample_variance(aa)))
    print('Std deviation value is {}'.format(sample_std_dev(aa)))
