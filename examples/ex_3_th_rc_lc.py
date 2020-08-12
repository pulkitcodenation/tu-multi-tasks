import concurrent.futures
import multiprocessing
import threading

counter = 0


def increment():
    global counter
    counter += 1


def increment_counter(fake_data, lock):
    for _ in range(100):
        with lock:
            increment()


if __name__ == "__main__":
    m = multiprocessing.Manager()
    lock = m.Lock()
    fake_data = [[x, lock] for x in range(500)]
    counter = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(increment_counter, fake_data)
        executor.map(lambda p: increment_counter(*p), fake_data)
    print(counter)
