#### BT 5
n = input("Ban hay dien vao mot con so: ")
n = int(n)
i = 1
tong = 0
while i < n+1:
    tong += i
    i += 1
print(tong)


#### BTCB
# Them thu vien de tao so ngau nhien
import random

# answer la so ngau nhien tu 0 den 10 duoc may tinh tu dong sinh ra
answer = random.randint(0, 10)  # lenh randint(0, 10) tra ve mot so tu 0 den 10
print("To dang nghi den 1 so nguyen nam trong khoang 0 den 10.")
# print(answer)

# Hoc sinh lap trinh tu dong nay tro xuong
counter = 0
while counter < 3:
    n = input("Do ban biet to dang nghi den so nao? ")
    n = int(n)
    if n == answer:
        print("Dung roi!")
        break
    elif n < answer:
        print("Thap qua!")
    else:
        print("Cao qua!")
    counter += 1


#### BTNC
# Them thu vien de tao so ngau nhien
import random

print("Chung minh cung choi oan tu ti nhe!")

# lenh nay cho ta 1 trong 3 so 0, 1, 2 mot cach ngau nhien
random_number = random.randint(0, 2)
if random_number == 0:
    computer_choice = "keo"
elif random_number == 1:
    computer_choice = "bua"
else:
    computer_choice = "bao"

# Goi y:
# so sanh du lieu nguoi dung nhap vao voi bien computer_choice:
# trong nhung truong hop nao thi may tinh va nguoi choi hoa nhau?
# trong nhung truong hop nao thi nguoi choi thang?
# trong nhung truong hop nao thi may tinh thang?

# Hoc sinh lap trinh tu dong nay tro xuong
# print(computer_choice)
gamer_choice = input("Ban ra gi? ")
if gamer_choice == computer_choice:
    print("Hoa roi!")
elif gamer_choice == "keo":
    if computer_choice == "bua":
        print("Ban da thua!")
    else:
        print("Ban da thang!")
elif gamer_choice == "bua":
    if computer_choice == "bao":
        print("Ban da thua!")
    else:
        print("Ban da thang!")
else:
    if computer_choice == "keo":
        print("Ban da thua!")
    else:
        print("Ban da thang!")