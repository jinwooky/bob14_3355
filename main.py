import argparse
import time
from typing import List, Callable, Dict

MAX_N = 10_000

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 쉼표로 구분된 데이터 읽어서 정렬
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    data = [int(x.strip()) for x in content.split(",")]

sorted_data = merge_sort(data)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def quick_sort(arr: List[int]) -> Tuple[List[int], float]:
    start_time = time.perf_counter()

    def _quick_sort(data: List[int]) -> List[int]:
        if len(data) <= 1:
            return data
        pivot = data[random.randrange(len(data))]
        left = [x for x in data if x < pivot]
        mid = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return _quick_sort(left) + mid + _quick_sort(right)

    sorted_arr = _quick_sort(arr[:])
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    return sorted_arr, elapsed_time

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

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def heap_sort():
    

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