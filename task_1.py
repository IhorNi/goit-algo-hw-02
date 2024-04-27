from queue import Queue
import random
import time
from faker import Faker


fake = Faker()
requests = Queue()


def generate_request():
    # Generate up to 2 new requests
    for _ in range(random.randint(0, 2)):
        request_info = fake.job()
        requests.put(request_info)
        print(f"Request '{request_info}' added to the queue")


def process_request():
    if not requests.empty():
        request_info = requests.get()
        print(f"Requst '{request_info}' is processed")
    else:
        print("Empty queue, waiting for new requests")


def print_progress():
    print("Processing", end="")
    for _ in range(3):
        time.sleep(1)
        print(".", end="", flush=True)
    print()


def main():
    # infinite loop, exit with Ctrl+C
    while True:
        generate_request()
        print_progress()
        process_request()


if __name__ == '__main__':
    main()
