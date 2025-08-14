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

def selection_sort():

def quick_sort():

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