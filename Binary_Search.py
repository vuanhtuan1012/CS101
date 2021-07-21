mang = [1, 10, 13, 20, 100, 102, 113]
so_can_tim = int(input("Số cần tìm: "))

found = False
while len(mang) > 0:
    index = len(mang) // 2
    print("Thử số: ", mang[index])
    if mang[index] == so_can_tim:
        found = True
        print("found it")
        break
    else:
        if mang[index] > so_can_tim:
            mang = mang[:index]
        else:
            mang = mang[index+1:]
if found == False:
    print("not found")
