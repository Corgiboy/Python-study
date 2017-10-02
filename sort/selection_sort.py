import random

def selection_sort(array):
    for start in range(len(array) - 1):
        min_idx = start
        for select_idx in range(start, len(array) - 1):
            if array[min_idx] > array[select_idx]:
                min_idx = select_idx
        array[start], array[min_idx] = array[min_idx], array[start]
    return array

def main():
    array = [random.randint(1, 100) for _ in range(20)]
    print('unsorted : ', array)
    print('sorted : ', selection_sort(array))

if __name__ == '__main__':
    main()
