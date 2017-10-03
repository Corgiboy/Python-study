import random

amount_of_nums = 10

def counting_sort(array, idx):
    size =len(array)
    tmp = [0 for _ in range(amount_of_nums)]
    result = [0 for _ in range(size)]
    get_num = lambda val : val % 10**(idx + 1) // 10**(idx)
    for val in array:
        tmp[get_num(val)] += 1
    for i in range(1, len(tmp)):
        tmp[i] += tmp[i - 1]
    for i in range(size - 1, -1, -1):
        result[tmp[get_num(array[i])] - 1] = array[i]
        tmp[get_num(array[i])] -= 1
    return result

def radix_sort(array):
    for idx in range(len(array)):
        array = counting_sort(array, idx)
    return array

def main():
    array = [random.randint(1e6, 9e6) for _ in range(20)]
    print('unsorted : ', array)
    print('sorted : ', radix_sort(array))

if __name__ == '__main__':
    main()
