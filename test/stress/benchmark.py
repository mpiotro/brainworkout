import time
from random import randint

from src.algorithms.sort.bubblesort import bubble_sort
from src.algorithms.sort.mergesort import merge_sort

if __name__ == "__main__":

    values = [randint(-10000, 10000) for value in range(1, 100000)]

    tic = time.perf_counter()

    bubble_sort(values)

    toc = time.perf_counter()

    print(f"Bubble sort finished in {toc - tic:0.4f} seconds")

    tic = time.perf_counter()

    merge_sort(values)

    toc = time.perf_counter()

    print(f"Merge sort finished in {toc - tic:0.4f} seconds")
