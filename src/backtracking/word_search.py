
__author__ = 'J.R.'


# search for a given word in a matrix of characters
def word_search(m, s):
    if m is None or s is None or len(m) == 0 or len(s) == 0:
        return None
    n = len(s)
    rows = len(m)
    cols = len(m[0])
    for i in range(rows):
        for j in range(cols):
            for k in range(n):
                if not _word_search(m, s, i, j, k):
                    break
                else:
                    return True
    return False


def _word_search(m, s, i, j, k):
    if k == len(s):
        return True
    if m is None or s is None or len(m) == 0 or len(s) == 0:
        return False
    n = len(s)
    rows = len(m)
    cols = len(m[0])
    if k >= n or i < 0 or i >= rows or j < 0 or j >= cols:
        return False
    if m[i][j] != s[k]:
        return False
    c = m[i][j]
    m[i][j] = '1'
    found = _word_search(m, s, i+1, j, k+1) \
        or _word_search(m, s, i-1, j, k+1) \
        or _word_search(m, s, i, j-1, k+1) \
        or _word_search(m, s, i, j+1, k+1)
    m[i][j] = c
    return found


if __name__ == '__main__':
    mm = [['t', 'c', 'a', 'o'], ['s', 'y', 'b', 'p'], ['t', 'm', 'l', 'e']]
    t = 'cable'
    print('Search for word {} in a given matrix of characters - {}'.format(t, word_search(mm, t)))
    t = 'handle'
    print('Search for word {} in a given matrix of characters - {}'.format(t, word_search(mm, t)))

