import argparse
import time
import multiprocessing
import os

def allocate_memory(mb):
    # Allocate memory in MB
    print(f"Allocating approximately {mb} MB of RAM...")
    a = [' ' * 1024 * 1024] * mb
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Memory chaos stopped.")

def burn_cpu():
    # Simple infinite CPU loop
    while True:
        pass

def simulate_cpu(cores):
    print(f"Spawning {cores} CPU-bound processes...")
    processes = []
    for _ in range(cores):
        p = multiprocessing.Process(target=burn_cpu)
        p.start()
        processes.append(p)
    try:
        for p in processes:
            p.join()
    except KeyboardInterrupt:
        print("CPU chaos stopped.")
        for p in processes:
            p.terminate()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Linux Chaos Generator for Memory/CPU")
    parser.add_argument("--memory", type=int, help="Amount of RAM in MB to allocate")
    parser.add_argument("--cpu", type=int, help="Number of CPU cores to burn")
    args = parser.parse_args()

    if args.memory:
        allocate_memory(args.memory)
    elif args.cpu:
        simulate_cpu(args.cpu)
    else:
        print("Please specify either --memory or --cpu")
