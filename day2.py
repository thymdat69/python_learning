def find_max(numbers):
    max_num = numbers[0]

    for n in numbers:
        if n > max_num:
            max_num = n

    return max_num

def find_min(numbers):
    min_num = numbers[0]
    for n in numbers:
        if n < min_num:
            min_num = n

    return min_num

def find_sum(numbers):
    sum_num = 0

    for n in numbers:
        sum_num += n

    return sum_num

def find_average(numbers):   
    avr_num = find_sum(numbers)/len(numbers)

    return avr_num


nums = input("Nhap cac so (cach nhau boi dau cach): ")
numbers = list(map(int, nums.split()))

max_value = find_max(numbers)
min_value = find_min(numbers)
sum_value = find_sum(numbers)
avr_value = find_average(numbers)

print("So lon nhat: ", max_value)
print("So nho nhat: ", min_value)
print("Tong: ", sum_value)
print("Trung binh: ", avr_value)