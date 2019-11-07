"""
    Binheap Runner
"""
from random import randint
import binheap

def random_list(low=0, high=100, count=20):
    return [randint(low, high) for _ in range(count)]

def main():
    nums = random_list(count=10)
    print(nums)

if __name__ == "__main__":
    main()