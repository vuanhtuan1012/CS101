mang = [1, 10, 13, 20, 100, 102, 113]
so_can_tim = int(input("Số cần tìm: "))

# while loop
found = False
index = 0
while index < len(mang):
    print("Thử số: ", mang[index])
    if mang[index] == so_can_tim:
        found = True
        print("found it")
        break
    index += 1
if found == False:
    print("not found")

# # for loop
# found = False
# for phan_tu in mang:
#     print("Thử số: ", phan_tu)
#     if phan_tu == so_can_tim:
#         found = True
#         print("found it")
#         break
# if found == False:
#     print("not found")