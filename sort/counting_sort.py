import random

def counting_sort(array):
    size = len(array)
    max_val = max(array)
    tmp = [0] * (max_val + 1)
    result = [0] * size
    for val in array:
        tmp[val] += 1
    for i in range(1, len(tmp)):
        tmp[i] += tmp[i - 1]
    for i in range(size - 1, -1, -1):
        result[tmp[array[i]] - 1] = array[i]
        tmp[array[i]] -= 1
    return result

def main():
    array = [random.randint(1, 100) for _ in range(20)]
    print('unsorted : ', array)
    print('sorted : ', counting_sort(array))

if __name__ == '__main__':
    main()
