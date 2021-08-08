#### BT1
nha_khoa_hoc = ["Tran Dai Nghia","Isaac Newton","Albert Einstein","Ngo Bao Chau","Hung Tran"]
nha_khoa_hoc.append("Le Thi Quynh Mai")
print(nha_khoa_hoc)


#### BT2
names = ["Vincent","Duc","Hung"]
for ten in names:
    for ki_tu in ten:
        print(ki_tu)


#### BT3
trials = [30,70,100,10]
snn = trials[0]
for phan_tu in trials:
    if snn > phan_tu:
        snn = phan_tu
print(snn)


#### BT4
number = [1,2,3,15,40,70,9,100,8]
tong = 0
for phan_tu in number:
    if phan_tu < 10:
        tong += phan_tu
print(tong)


#### BT5
trials = [[2,4,6],[3,5,7]]
for mang in trials:
    for phan_tu in mang:
        print(phan_tu)


#### BTCB
data = [[10, 62, 30, 65],
        [100, 100],
        [86, 85, 87]]
diems = []
for vaccine in data:
    if len(vaccine) < 3:
        diems.append(0.0)
    else:
        tong = 0
        for diem_thu_nghiem in vaccine:
            tong += diem_thu_nghiem
            if diem_thu_nghiem < 50:
                tong = 0
                break
        diems.append(tong/len(vaccine))
print(diems)


#### BTNC
plaintext = "TRAU"
output = ""
for ki_tu in plaintext:
    if ki_tu == "Y":
        output += "A"
    elif ki_tu == "Z":
        output += "B"
    else:
        output += chr(ord(ki_tu) + 2)
print(output)
