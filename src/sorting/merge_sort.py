from src.sorting.base_sorting import Sorting


# MergeSort sorting algorithm implementation using recursive approach with additional array
# Time ~O(nlogn)
# Mem  ~O(n)
class MergeSort(Sorting):

    def __init__(self):
        pass

    def sort(self, a):
        if a is None or len(a) == 0:
            return

        lo = 0
        hi = len(a) - 1
        t = []
        self._merge_sort(a, t, lo, hi)

    def _merge_sort(self, a, t, lo, hi):
        if lo >= hi:
            return
        mid = lo + (hi - lo) // 2
        self._merge_sort(a, t, lo, mid)
        self._merge_sort(a, t, mid + 1, hi)
        self._merge(a, t, lo, mid + 1, hi)

    def _merge(self, a, t, lo, hi, hi_end):
        if lo >= hi:
            return

        start = lo
        lo_end = hi - 1
        count = hi_end - lo + 1
        while lo <= lo_end and hi <= hi_end:
            if a[lo] < a[hi]:
                t.insert(start, a[lo])
                lo += 1
            else:
                t.insert(start, a[hi])
                hi += 1
            start += 1

        while lo <= lo_end:
            t.insert(start, a[lo])
            start += 1
            lo += 1

        while hi <= hi_end:
            t.insert(start, a[hi])
            start += 1
            hi += 1

        while count > 0:
            a[hi_end] = t[hi_end]
            hi_end -= 1
            count -= 1


if __name__ == '__main__':

    aa = [2, 3, 1, 8, 9, 4, 6, 5]
    sorting = MergeSort()
    print('Original array {}'.format(aa))
    sorting.sort(aa)
    print('Sorted array {}'.format(aa))