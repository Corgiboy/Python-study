import random

def selection_sort(array):
    for idx in range(len(array)):
        min_idx = idx
        for i in range(idx, len(array)):
            if array[min_idx] > array[i]:
                min_idx = i
        array[idx], array[min_idx] = array[min_idx], array[idx]
    return array

def main():
    array = [random.randint(1, 100) for _ in range(20)]
    print('unsorted : ', array)
    print('sorted : ', selection_sort(array))

if __name__ == '__main__':
    main()
