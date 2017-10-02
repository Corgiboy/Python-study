import random

def isertion_sort(array):
    for index in range(1, len(array)):
        cur_val = array[index]
        while index > 0 and array[index - 1] > cur_val:
            array[index] = array[index - 1]
            index -= 1
        array[index] = cur_val
    return array

def main():
    array = [random.randint(1, 100) for _ in range(20)]
    print('unsorted : ', array)
    print('sorted : ', isertion_sort(array))

if __name__ == '__main__':
    main()
