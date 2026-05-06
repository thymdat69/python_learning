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
    total = 0
    for n in numbers:
        total += n
    return total

numbers = []

while True:
    print("\n--- MENU ---")
    print("1. Nhap danh sach so")
    print("2. Tim max")
    print("3. Tim min")
    print("4. Tinh tong")
    print("5. Thoat")

    choice = input("Chon: ")

    if choice == "1":
        nums = input("Nhap so: ")
        try:
            numbers = (list(map(int, nums.split())))
        except:
            print("Nhap sai, vui long chi nhap so")

    elif choice in ["2", "3", "4"]:
        if len(numbers) == 0:
            print("Chua co du lieu")
        else:
            if choice == "2":
                print("Max la: ", find_max(numbers))
            elif choice == "3":
                print("Min la:", find_min(numbers))
            elif choice == "4":
                print("Tong la:", find_sum(numbers))

    elif choice == "5":
        print("Thoat...")
        break

    else:
        print("Sai cu phap")