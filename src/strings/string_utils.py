
__author__ = 'J.R.'


# reverse string
def reverse(s):
    ch = list(map(lambda c: c if c.isalpha() else ' ', s))
    _reverse(ch, 0, len(s) - 1)
    return ''.join(ch)


# reverse string private method
def _reverse(s, lo, hi):
    i = lo
    j = hi
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s


# reverse words in a given sentence
def reverser_words_in_sentence(s):
    if s is None or len(s) == 0:
        return s
    n = len(s)
    start = 0
    ch = list(map(lambda c: c if c.isalpha() else ' ', s))
    ch = _reverse(ch, 0, n - 1)
    for i in range(n + 1):
        if i == n or ch[i].isspace():
            ch = _reverse(ch, start, i - 1)
            start = i + 1
    return ''.join(ch)

if __name__ == '__main__':
    ss = 'I am working at home'
    print('Reversed string  - {}'.format(reverse(ss)))
    print('Reversed words in string  - {}'.format(reverser_words_in_sentence(ss)))
