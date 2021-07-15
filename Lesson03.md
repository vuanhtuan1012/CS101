# Bài 3: Vaccine Nào Tốt Nhất

- [x] [Mảng (Array)](#m%E1%BA%A3ng-array): khái niệm, khởi tạo, truy cập, phương thức và hàm.
- [x] [Mảng hai chiều (2D array)](#m%E1%BA%A3ng-hai-chi%E1%BB%81u-2d-array)
- [x] [Vòng lặp `for`](#v%C3%B2ng-l%E1%BA%B7p-for): cấu trúc, thực thi.
- [x] [Thuật toán tính tổng](#thu%E1%BA%ADt-to%C3%A1n-t%C3%ADnh-t%E1%BB%95ng): ý tưởng, thuật toán, mở rộng tính trung bình cộng.
- [x] [Thuật toán tìm số lớn nhất](#thu%E1%BA%ADt-to%C3%A1n-t%C3%ACm-s%E1%BB%91-l%E1%BB%9Bn-nh%E1%BA%A5t): ý tưởng, thuật toán sử dụng vòng lặp `for`, thuật toán sử dụng vòng lặp `while`.

## Tài nguyên

- [[Lesson3] Preparation slide](https://docs.google.com/presentation/d/e/2PACX-1vRiCUOJUjtOD7u3mqnoHG9pLjbwb7cs6UDoE-Xcz-9T6EhHg8zeSO0HhLYzFWaiWOf2u4gwBM-siF42/embed?start=false&loop=false&delayms=3000&slide=id.ge0eb9e71c2_0_1680)
- [[SUM-21-101] Lesson 3 - Game Đoàn Tàu Bí Mật](https://scratch.mit.edu/projects/550932789)
- [[Lesson3] Final slide](https://docs.google.com/presentation/d/e/2PACX-1vSrd1jFf0Kwjp7EFosMN7jRH8cuW-NfWnJJkKYUG6IUrgKlGQnPvy-6CnMYBSOvxBettbbwIUuYyTgo/embed?start=false&loop=false&delayms=3000&slide=id.ge0eb9e71c2_0_1680)
- [Vaccine trials](https://docs.google.com/spreadsheets/d/1R_Z72Lx45UyqqTVvv1IdcJXeFin4HHJ0R9rZkjErozA/edit?usp=sharing)
- [[SUM21] Lesson 3 - Thuật toán tìm số lớn nhất](https://scratch.mit.edu/projects/551839991/)

## Mảng (Array)

### Khái niệm

Nếu coi biến giống như một chiếc hộp chứa dữ liệu thì mảng giống như một chiếc hộp dài chứa những chiếc hộp con được xếp cạnh nhau.
- mảng gồm nhiều phần tử (chiếc hộp con).
- mỗi phần tử đều có số thứ tự (index) để phân biệt với nhau.
- số thứ tự (index) trong mảng được **bắt đầu từ 0**.
- mảng có thể chứa dữ liệu dạng: số nguyên (`int`), số thực (`float`), chuỗi kí tự (`str`), logic (`bool`), etc.

### Khởi tạo

- Cú pháp: `tên_mảng = [danh_sách_các_phần_tử]`
    - `danh_sách_các_phần_tử` là chuỗi các phần tử được phân tách nhau bằng dấu phẩy `,`. Ví dụ: `1, 2, 3, 4`
    - nếu không đưa vào `danh_sách_các_phần_tử` chúng ta sẽ có một mảng trống, không chứa phần tử nào.
- **Chú ý:** `danh_sách_các_phần_tử` được đặt giữa cặp ngoặc vuông `[]`.

```Python
m1 = [2, 3, 4] # khởi tạo mảng m1 gồm 3 phần tử nguyên
m2 = [] # khởi tạo mảng m2 không chứa phần tử nào, mảng trống
m3 = [2, "Chi", 1.0, False] # khởi tạo mảng m3 gồm 4 phần tử mang các kiểu dữ liệu khác nhau
```

### Truy cập

Có 2 cách để truy cập các phần tử trong mảng: sử dụng số thứ tự (index), hoặc sử dụng vòng lặp `for`.

- Cách 1: sử dụng số thứ tự (index) của phần tử: `tên_mảng[i-1]` trả về phần tử thứ `i` trong mảng.
```Python
mang = [2, "Chi", 1.0, False]
mang[0] # return 2
mang[1] # return "Chi"
mang[2] # return 1.0
mang[3] # return False
mang[4] # error IndexError
```
- Cách 2: sử dụng vòng lặp `for`: xem phần [vòng lặp `for`](#v%C3%B2ng-l%E1%BA%B7p-for).

### Phương thức và Hàm

- `append()` : phương thức thêm phần tử vào cuối mảng.
    - Cú pháp:  `tên_mảng.append(phần_tử)`.
    - **Chú ý:** có dấu chấm `.` giữa `tên_mảng` và `append`.
    - Ví dụ: `mang.append(5)` thêm phần tử `5` vào cuối mảng `mang`.
- `len()`: hàm đếm số phần tử của mảng.
    - Cú pháp: `len(tên_mảng)`.
    - Ví dụ: `len(mang)` trả về 4 là tổng số phần tử trong mảng `mang`.

```Python
mang = [] # khởi tạo mảng trống
len(mang) # return 0
mang.append(82) # thêm số nguyên 82 vào cuối mảng
mang.append(8.5) # thêm số thực 8.5 vào cuối mảng
mang.append("hello world") # thêm chuỗi "hello world" vào cuối mảng
mang.append(True) # thêm giá trị logic True vào cuối mảng
len(mang) # return 4
```

## Mảng hai chiều (2D Array)

Một mảng có thể chứa các mảng khác. Khi đó ta có mảng hai chiều (2D array). Các hàm, phương thức của mảng cũng đúng với mảng hai chiều.

```Python
# khởi tạo mảng 2 chiều tên data chứa 3 mảng con
data = [[80, 85, 87],
        [70, 80, 90],
        [95, 75, 60]]
print(data[0]) # in ra mảng con đầu tiên
print(data[1][0]) # in ra phần tử đầu tiên của mảng con thứ hai
data.append([60, 50, 40]) # thêm một mảng con vào cuối mảng data
print(len(data)) # return 4
```

## Vòng lặp `for`

> [Video bài giảng](https://youtu.be/mgOtiIuhJZc?t=5235) :  nên đặt tốc độ phát ở 1.25 hoặc 1.5

Vòng lặp `for` dùng để duyệt qua tất cả các phần tử của mảng mà không cần đưa vào số thứ tự của chúng.
- Cấu trúc:
```Python
for phần_tử in tên_mảng:
    mã_lệnh_1
    mã_lệnh_2
    ...
```
- Thực thi: vòng lặp `for` sẽ đi qua từng phần tử trong mảng theo đúng số thứ tự của các phần tử.
- Ví dụ dưới dây sẽ in ra các phần tử trong mảng `mang` theo đúng thứ tự của chúng trong mảng.
```Python
mang = [80, 85, 87]
for phan_tu in mang:
    print(phan_tu)
```

**Vòng lặp `for` cũng được dùng để duyệt qua các kí tự của một chuỗi kí tự**.
```Python
ho_ten = "Vũ Khánh Chi"
for ki_tu in ho_ten:
    print(ki_tu)
```

## Thuật toán tính tổng

- Ý tưởng:
    - khởi tạo biến `tong = 0` để lưu tổng các phần tử trong mảng
    - dùng vòng lặp `for` duyệt qua các phần tử trong mảng. Mỗi khi gặp một phần tử, ta sẽ cộng thêm phần tử đó vào mảng.
- Thuật toán
```Python
mang = [80, 85, 87]
tong = 0
for phan_tu in mang:
    tong += phan_tu
print(tong)
```
- Mở rộng **tính trung bình cộng**: sau khi tìm được tổng ta chia cho tổng số phần tử sẽ được trung bình cộng của mảng.
```Python
mang = [80, 85, 87]
tong = 0
for phan_tu in mang:
    tong += phan_tu
tbc = tong / len(mang)
print(tbc)
```

## Thuật toán tìm số lớn nhất

- Ý tưởng:
    - dùng một biến `so_lon_nhat` để lưu giá trị đầu tiên của mảng.
    - dùng vòng lặp `for` hoặc `while` đi qua các phần tử của mảng, nếu gặp phần tử lớn hơn `so_lon_nhat` thì đặt lại giá trị của `so_lon_nhat` bằng phần tử này.
    - kết thúc vòng lặp, biến `so_lon_nhat` sẽ chứa giá trị lớn nhất của mảng.
- Thuật toán sử dụng vòng lặp `for`
```Python
mang = [1, 4, 8, 12, 3, 5]
so_lon_nhat = mang[0]
for phan_tu in mang:
    if phan_tu > so_lon_nhat:
        so_lon_nhat = phan_tu
print(so_lon_nhat)
```
- Thuật toán sử dụng vòng lặp `while`
```Python
mang = [1, 4, 8, 12, 3, 5]
so_lon_nhat = mang[0]
index = 0
while index < len(mang):
    phan_tu = mang[index]
    if phan_tu > so_lon_nhat:
        so_lon_nhat = phan_tu
    index += 1
print(so_lon_nhat)
```