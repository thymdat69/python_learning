def add_number(numbers):
    try:
        num = int(input("Nhap so can them: "))
        numbers.append(num)
    except:
        print("Vui long chi nhap so")

def delete_number(numbers):
    try:
        num = int(input("Nhap so can xoa")) 
        if num in numbers:
            numbers.remove(num)
        else:
            print("So khong ton tai")
    except:
        print("Vui long nhap so")

def find_max(numbers):
    max_num = numbers[0]
    for n in numbers:
        if n > max_num:
            max_num = n
    return max_num

numbers = []

while True:
    print("\n--MENU--")
    print("1. Nhap danh sach so")
    print("2. Them 1 so")
    print("3. Xoa 1 so")
    print("4. Xem danh sach")
    print("5. Tim max")
    print("6. Thoat")

    choice = input("Chon: ")

    if choice == "1":
        nums = input("Nhap so: ")
        try:
            numbers = (list(map(int, nums.split())))
        except:
            print("Nhap sai, vui long chi nhap so")
    elif choice in ["2", "3", "4", "5"]:
        if len(numbers) == 0:
            print("Chua co du lieu")
        else:
            if choice == "2":
                add_number(numbers)
            elif choice == "3":
                delete_number(numbers)
            elif choice == "4":
                print(numbers)
            elif choice == "5":
                print("Max la: ", find_max(numbers))
    elif choice == "6":
        break
    else:
        print("Sai cu phap")