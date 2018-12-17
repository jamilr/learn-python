__author__ = 'J.R.'


# search for a given group of words in a matrix of characters
def search_group_of_words(matrix, words):
	if matrix is None or words is None or len(matrix) == 0 or len(words) == 0:
		return None
	found_words = list()
	words_count = len(words)
	for idx in range(words_count):
		if word_search(matrix, words[idx]):
			found_words.append(words[idx])
	return found_words


# search for a given word in a matrix of characters
def word_search(matrix, word):
	if matrix is None or word is None or len(matrix) == 0 or len(word) == 0:
		return None
	rows = len(matrix)
	cols = len(matrix[0])
	for i in range(rows):
		for j in range(cols):
			if _word_search(matrix, word, i, j, 0):
				return True
	return False


def _word_search(matrix, word, i, j, k):
	n = len(word)
	if k == n:
		return True
	if matrix is None or word is None or len(matrix) == 0 or len(word) == 0:
		return False
	rows = len(matrix)
	cols = len(matrix[0])
	if k > n or i < 0 or i >= rows or j < 0 or j >= cols:
		return False
	if matrix[i][j] != word[k]:
		return False
	c = matrix[i][j]
	matrix[i][j] = '1'
	found = _word_search(matrix, word, i + 1, j, k + 1) \
			or _word_search(matrix, word, i - 1, j, k + 1) \
			or _word_search(matrix, word, i, j - 1, k + 1) \
			or _word_search(matrix, word, i, j + 1, k + 1)
	matrix[i][j] = c
	return found


def message(exists):
	return 'Found' if exists else 'Not Found'


def print_input_matrix(matrix):
	concat_m = [' '.join(a) for a in matrix]
	for a in concat_m:
		print(a)


if __name__ == '__main__':
	matrix = [['t', 'c', 'a', 'o'], ['s', 'y', 'b', 'p'], ['t', 'm', 'l', 'e']]
	print_input_matrix(matrix)
	t = 'cable'
	print('Search for word {} - {}'.format(t, message(word_search(matrix, t))))
	t = 'handle'
	print('Search for word {} - {}'.format(t, message(word_search(matrix, t))))
	group = ['cable', 'handle', 'cab']
	print('Search for words {} Found words - {}'.format(group, search_group_of_words(matrix, group)))

