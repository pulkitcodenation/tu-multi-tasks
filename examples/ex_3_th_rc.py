import concurrent.futures


counter = 0


def increment_counter(fake_data):
    global counter
    for _ in range(100):
        counter += 1


if __name__ == "__main__":
    fake_data = [x for x in range(50)]
    counter = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(increment_counter, fake_data)
    print(counter)
