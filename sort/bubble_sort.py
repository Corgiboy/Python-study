import random

def bubble_sort(array):
    for edge in range(len(array) - 1, 0, -1):
        for index in range(edge):
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = \
                    array[index + 1], array[index]
    return array

def main():
    array = [random.randint(1, 100) for _ in range(20)]
    print('unsorted : ', array)
    print('sorted : ', bubble_sort(array))

if __name__ == '__main__':
    main()
