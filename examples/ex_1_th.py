#!/usr/bin/env python3
import concurrent.futures
import time


def process(number):
    start_time = time.time()
    print(f"Entering {number}")
    answer = sum(i * i for i in range(number))
    duration = time.time() - start_time
    print(f"Exiting {number}: {duration}")
    return answer


def find_sums(numbers):
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(process, numbers)


if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]

    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")