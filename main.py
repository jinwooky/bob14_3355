import argparse
import time
from typing import List, Callable, Dict

MAX_N = 10_000

def merge_sort():

def selection_sort():

def quick_sort():

def bubble_sort(arr: List[int]) -> List[int]:
    a = arr[:]  # preserve original
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:  # early exit
            break
    return a

def insertion_sort():

def heap_sort(arr: List[int]) -> List[int]:

    a = arr[:]  # Copy to preserve original
    n = len(a)

    # Maintain max-heap property
    def sift_down(start, end):
        root = start
        while True:
            child = 2 * root + 1  # Left child
            if child > end:
                break
            if child + 1 <= end and a[child] < a[child + 1]:  # Select larger child
                child += 1
            if a[root] < a[child]:
                a[root], a[child] = a[child], a[root]
                root = child
            else:
                break

    # Build max-heap
    for start in range((n - 2) // 2, -1, -1):
        sift_down(start, n - 1)

    # Extract elements from heap
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        sift_down(0, end - 1)

    return a


def read_data(path: str) -> List[int]:
    nums: List[int] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            for tok in line.split(","):
                tok = tok.strip()
                if tok:
                    nums.append(int(tok))
                    if len(nums) >= MAX_N:
                        return nums
    return nums


def main():
    parser = argparse.ArgumentParser(description="정렬 실습: 파일만 넣으면 5개 정렬 모두 실행")
    parser.add_argument("file", nargs="?", default="data.txt", help="데이터 파일 경로 (기본: data.txt)")
    args = parser.parse_args()
    

    arr = read_data(args.file)


if __name__ == "__main__":
    main()