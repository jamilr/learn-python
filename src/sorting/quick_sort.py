from src.sorting.base_sorting import Sorting


# QuickSort sorting algorithm implementation using in-place recursive approach
# Time ~O(nlogn)
# Mem  ~O(1)
class QuickSort(Sorting):

    def __init__(self):
        pass

    def sort(self, a):
        if a is None or len(a) == 0:
            return

        n = len(a)
        lo = 0
        hi = n - 1
        self._quick_sort(a, lo, hi)

    def _quick_sort(self, a, lo, hi):
        if a is None or len(a) == 0:
            return

        i = lo
        j = hi
        while i <= j:
            p = lo + (hi - lo) // 2

            while a[i] < a[p]:
                i += 1

            while a[j] > a[p]:
                j -= 1

            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1

        if j > lo:
            self.quick_sort(a, lo, j)

        if i < hi:
            self.quick_sort(a, i, hi)


if __name__ == '__main__':

    aa = [2, 3, 1, 8, 9, 4, 6, 5]
    sorting = QuickSort()
    print('Original array {}'.format(aa))
    sorting.sort(aa)
    print('Sorted array {}'.format(aa))
