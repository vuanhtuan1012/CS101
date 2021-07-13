# Bài 3: Vaccine Nào Tốt Nhất

- [x] [Mảng (Array)](#m%E1%BA%A3ng-array)
- [x] [Mảng hai chiều (2D array)](#m%E1%BA%A3ng-hai-chi%E1%BB%81u-2d-array)
- [x] [Vòng lặp `for`](#v%C3%B2ng-l%E1%BA%B7p-for)
- [x] Thuật toán tìm số lớn nhất

## Tài nguyên

- [[Lesson3] Preparation slide](https://docs.google.com/presentation/d/e/2PACX-1vRiCUOJUjtOD7u3mqnoHG9pLjbwb7cs6UDoE-Xcz-9T6EhHg8zeSO0HhLYzFWaiWOf2u4gwBM-siF42/embed?start=false&loop=false&delayms=3000&slide=id.ge0eb9e71c2_0_1680)
- [[SUM-21-101] Lesson 3 - Game Đoàn Tàu Bí Mật](https://scratch.mit.edu/projects/550932789)
- [[Lesson3] Final slide](https://docs.google.com/presentation/d/e/2PACX-1vSrd1jFf0Kwjp7EFosMN7jRH8cuW-NfWnJJkKYUG6IUrgKlGQnPvy-6CnMYBSOvxBettbbwIUuYyTgo/embed?start=false&loop=false&delayms=3000&slide=id.ge0eb9e71c2_0_1680)
- [Vaccine trials](https://docs.google.com/spreadsheets/d/1R_Z72Lx45UyqqTVvv1IdcJXeFin4HHJ0R9rZkjErozA/edit?usp=sharing)
- [[SUM21] Lesson 3 - Thuật toán tìm số lớn nhất](https://scratch.mit.edu/projects/551839991/)

## Mảng (Array)

Nếu coi biến giống như một chiếc hộp chứa dữ liệu thì mảng giống như một chiếc hộp dài chứa những chiếc hộp con được xếp cạnh nhau.
- mảng gồm nhiều phần tử (chiếc hộp con).
- mỗi phần tử đều có số thứ tự (index) để phân biệt với nhau.
- số thứ tự trong mảng được **bắt đầu từ 0**.
- mảng có thể chứa dữ liệu dạng: số nguyên (`int`), số thực (`float`), chuỗi kí tự (`str`), logic (`bool`), etc.
- khởi tạo mảng: `tên_mảng = [danh_sách_các_phần_tử]`
	- `danh_sách_các_phần_tử` là chuỗi các phần tử được phân tách nhau bằng dấu phẩy `,`.
	- nếu không đưa vào `danh_sách_các_phần_tử` chúng ta sẽ có một mảng trống, không chứa phần tử nào.
- truy cập phần tử trong mảng bằng cách sử dụng tên mảng, số thứ tự (index) của phần tử. Ví dụ: `tên_mảng[i-1]` trả về phần tử thứ `i` trong mảng.
- thêm phần tử vào mảng bằng cách sử dụng phương thức `append()`: `tên_mảng.append(phần_tử)`. **Chú ý:** có dấu chấm `.` giữa `tên_mảng` và `append`.
- đếm số phần tử của mảng bằng cách sử dụng hàm `len()`: `len(tên_mảng)`.
```Python
trials = [80, 85, 87] # khởi tạo mảng tên trials chứa 3 phần tử
print(trials[0]) # in ra giá trị của phần tử đầu tiên
print(trials[3]) # lỗi IndexError
trials.append(82) # thêm một số nguyên vào cuối mảng
trials.append(8.5) # thêm một số thực vào cuối mảng
trials.append("hello world") # thêm một chuỗi kí tự vào cuối mảng
len(trials) # return 6
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

- Cấu trúc:
```Python
for giá_trị in tên_mảng:
	mã_lệnh_1
	mã_lệnh_2
	...
```
- Thực thi: vòng lặp `for` sẽ đi qua từng phần tử trong mảng, biến `giá_trị` sẽ lần lượt nhận giá trị của các phần tử.
- Ví dụ dưới đây dùng để tính trung bình cộng của các phần tử trong mảng `trials`

```Python
trials = [80, 85, 87]
tong = 0
for gia_tri in trials:
	tong += gia_tri
tbc = tong / len(trials)
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