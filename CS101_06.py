#### Read file
# doc du lieu tu file vao mang applicants
applicants = []
with open("applicants.csv", "r") as file_reader:
    lines = file_reader.readlines()
    for line in lines:
        applicant = line.strip()
        applicants.append(applicant)

# lay ra tat ca cac ung vien den tu TP HCM
applicants_HCM = []
for applicant in applicants:
    city = applicant.split(",")[1]
    if city == "TP Ho Chi Minh":
        applicants_HCM.append(applicant)

# lay ra 20 ung vien dau tien
## cach 1
first_20_HCM = []
for applicant in applicants_HCM:
    first_20_HCM.append(applicant)
    if len(first_20_HCM) == 20:
        break
## cach 2
if len(applicants_HCM) < 20:
    first_20_HCM = applicants_HCM
else:
    first_20_HCM = applicants_HCM[:20]
    
    
#### Write file
# ghi du lieu trong mang first_20_HCM vao file first_20_HCM.txt
with open("frist_20_HCM.txt", "w") as file_writer:
    for applicant in first_20_HCM:
        file_writer.write(applicant + "\n")


#### Scope
name = "Chi"
def say_hi_1():
    print("Hi " + name)

def say_hi_2():
    name = "Tuan"
    print("Hi " + name)

def say_hi_3():
    name = "Thao"
    print("Hi " + name)

say_hi_1()
say_hi_2()
say_hi_3()


#### BT1
def process_string(string):
    stripped_string = string.strip()
    things = stripped_string.split()
    return things

# commands to test in shell
process_string("  Hello Steamese ")
process_string("Candy               banana                           apple")


#### BT2
def get_even(array):
    even_numbers = []
    for number in array:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

# command to test in shell
get_even([1, 4, 6, 7, 9, 3])


#### BT3
def reverse_array(array):
    reversed_array = []
    index = len(array) - 1
    while index >= 0:
        reversed_array.append(array[index])
        index -= 1
    return reversed_array

# command to test in shell
reverse_array([1, 2, 3, 4, 5, 6])


#### BT4
def function1(string):
    output = string + " Tom"
    return output

def function2(string):
    output = string + " Jerry"
    return output

# command to test in shell
string = "Hello"
print(function1(string))
print(function2(string))


#### BT5
def find_median(array):
    if len(array) == 0:
        return None
    if len(array) % 2 == 0:
        index = len(array) // 2
        median = (array[index-1] + array[index])/2
        return median
    if len(array) % 2 == 1:
        index = len(array) // 2
        median = array[index]
        return median

# commands to test in shell
find_median([2, 4, 5, 7, 8, 9])
find_median([1, 3, 4, 6, 7])


#### BTCB
def filter(array):
    giang_vien_hn = []
    for giang_vien in array:
        thong_tin = giang_vien.split(",")
        thanh_pho = thong_tin[2]
        if thanh_pho == "Hanoi":
            giang_vien_hn.append(giang_vien)
    return giang_vien_hn

# command to test in shell
filter(["01,quan,Hanoi", "02,tri,HCM", "03,nam,Hanoi"])


#### BTNC
import random

def filter_random(array):
    # lay tat ca cac tro giang Ha Noi
    tro_giang_hn = []
    for tro_giang in array:
        thong_tin = tro_giang.split(",")
        thanh_pho = thong_tin[2].strip()
        if thanh_pho == "Hanoi":
            tro_giang_hn.append(tro_giang)
    
    # tra ve 3 tro giang Ha Noi ngau nhien
    if len(tro_giang_hn) <= 3:
        return tro_giang_hn
    else:
        random.shuffle(tro_giang_hn)
        return tro_giang_hn[:3]

# commands to test in shell
filter_random(["01, quan, Hanoi", "02, tri, HCM",
               "03, nam, Hanoi", "04, thuy, Hanoi",
               "05, nga, Hanoi", "06, duc, Hanoi",
               "07, giang, HCM"])
filter_random(["01, quan, Hanoi", "02, tri, HCM", "03, nam, Hanoi"])