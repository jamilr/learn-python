
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


# longest sub-string with at most k distinct characters
def longest_substring_with_at_most_k_distinct_distinct_characters(s, k):
    if s is None or len(s) == 0:
        return 0
    n = len(s)
    start = 0
    max_len = 0
    max_len_end = 0
    char_dict = {}
    for i in range(n):
        sh = s[i]
        char_dict[sh] = i
        if len(char_dict) > k:
            j = n - 1
            vv = list(char_dict.values())
            vv_size = len(vv)
            for l in range(0, vv_size):
                if vv[l] < j:
                    j = vv[l]
            ssh = s[j]
            del char_dict[ssh]
            start = j + 1
        if max_len < (i - start + 1):
            max_len = i - start + 1
            max_len_end = i
    return s[max_len_end - max_len + 1:max_len_end + 1]


if __name__ == '__main__':
    ss = 'I am working at home'
    print('Reversed string  - {}'.format(reverse(ss)))
    print('Reversed words in string  - {}'.format(reverser_words_in_sentence(ss)))
    ss = 'aaabbaabaabchdsr'
    print('Longest substring with at most {} distinct characters in a given string {} --> {}'
          .format(2, ss, longest_substring_with_at_most_k_distinct_distinct_characters(ss, 2)))

