import argparse
import time
from typing import List, Callable, Dict

MAX_N = 10_000

def merge_sort():

def selection_sort():

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

def bubble_sort():

def insertion_sort():

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