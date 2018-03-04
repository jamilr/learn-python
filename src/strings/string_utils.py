
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


# find first duplicate character in a string
def first_duplicate_char_in_string(s):
    if s is None or len(s) == 0:
        return -1
    n = len(s)
    a_set = set()
    for sh in s:
        if sh in a_set:
            return sh
        else:
            a_set.add(sh)
    return -1


# find first unique character in a given string
def first_unique_char_in_a_string(s):
    if s is None or len(s) == 0:
        return -1
    n = len(s)
    char_dict = {}
    first_unique_char_index = -1
    for i in range(n):
        sh = s[i]
        char_dict[sh] = char_dict.get(sh, 0) + 1
    for key in char_dict.keys():
        if char_dict.get(key) == 1:
            return key
    return -1


# check if string is palindrome
def is_palindrome(s):
    if s is None or len(s) == 0:
        return True
    lo = 0
    hi = len(s) - 1
    while lo < hi:
        lch = s[lo]
        rch = s[hi]
        if lch != rch:
            return False
        lo += 1
        hi -= 1
    return True


# check if two strings s, and t are anagrams
def is_anagram(s, t):
    if s is None and t is None:
        return True
    if s is None or t is None:
        return False
    n = len(s)
    m = len(t)
    if n != m:
        return False
    char_dict = {}
    for i in range(n):
        sh = s[i]
        char_dict[sh] = char_dict.get(sh, 0) + 1
    for i in range(m):
        sh = t[i]
        if sh not in char_dict.keys():
            return False
        char_dict[sh] = char_dict.get(sh) - 1
        if char_dict.get(sh) == 0:
            del char_dict[sh]
    return not bool(char_dict)


# group anagrams together and return sorted array of strings
def group_anagrams(s):
    return sorted(s, key=lambda input_string: sorted(input_string))


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
    print('First unique character in {}  is  {}'.format(ss, first_unique_char_in_a_string(ss)))
    print('First duplicate character in {}  is  {}'.format(ss, first_duplicate_char_in_string(ss)))

    ss = 'tac'
    tt = 'cat'
    print('Two strings are anagrams {} {} - {}'.format(ss, tt, is_anagram(ss, tt)))
    ss = 'tac'
    tt = 'ads'
    print('Two strings are anagrams {} {} - {}'.format(ss, tt, is_anagram(ss, tt)))

    list_s = ['cat', 'pin', 'tac', 'nip', 'atc', 'dab', 'bad']
    print('Group anagrams - {}'.format(group_anagrams(list_s)))

    ss = '1234321'
    print('Check is palindrome - {}'.format(is_palindrome(ss)))
    ss = '12343213'
    print('Check is palindrome - {}'.format(is_palindrome(ss)))
