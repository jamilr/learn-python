
import copy

__author__ = 'J.R.'


# create all permutations for a given array of elements
def permute(a):
    if a is None or len(a) == 0:
        return None
    a = sorted(a)
    n = len(a)
    result = list()
    seq = list()
    used = [False] * n
    _permute(a, seq, result, used)
    return result


def _permute(a, seq, result, used):
    if len(seq) == len(a):
        result.append(copy.deepcopy(seq))
        return
    n = len(a)
    for i in range(n):
        if used[i] or (i > 0 and a[i] == a[i-1] and not used[i-1]):
            continue
        seq.append(a[i])
        used[i] = True
        _permute(a, seq, result, used)
        used[i] = False
        seq.pop()


if __name__ == '__main__':
    mm = ['1', '2', '1']
    expected = [['1', '1', '2'], ['1', '2', '1'], ['2', '1', '1']]
    print(permute(mm))
