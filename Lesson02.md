# Bài 2: Vá Lỗ Hổng Bảo Mật

- [x] Nhận dữ liệu
- [x] [Lưu dữ liệu](#l%C6%B0u-d%E1%BB%AF-li%E1%BB%87u): biến, kiểu dữ liệu, các hàm kiểm tra, chuyển kiểu dữ liệu
- [x] [Câu điều kiện](#c%C3%A2u-%C4%91i%E1%BB%81u-ki%E1%BB%87n): cú pháp, phép so sánh, toán tử kết hợp, rẽ nhánh
- [ ] Vòng lặp

## Tài nguyên

- [[Lesson 2] Final slide](https://docs.google.com/presentation/d/e/2PACX-1vQDVcShEMycySKE-f9K4Ba0-IVWYFvrzdrTC_8FJxvR5UihpsaF6athTnzUGdpNEvdpN7CCNFxem53t/embed?start=false&loop=false&delayms=3000&slide=id.ge1110aec4e_0_373)
- [[Lesson 2] Flash Card + Common Mistake](https://docs.google.com/presentation/d/e/2PACX-1vSeld3F9SPXgwo2hpm-VvcUhh5H9z48dhpTvfwa5uVEtkvbgbqcEkvF6BMq89sbKiKhBuAqZfb7GmY6/embed?start=false&loop=false&delayms=3000&slide=id.gb2bf68220d_0_0)
- [[SUM21] Lesson2_Cửa Thông Minh](https://scratch.mit.edu/projects/549780910/)
- [[SUM21] Lesson 2_Chiến Đấu Với Virus](https://scratch.mit.edu/projects/549717830)

## Nhận dữ liệu

- `input()`: đưa ra hướng dẫn và chờ người dùng nhập dữ liệu vào.
```Python
input("Bạn tên là gì? ")
```

## Lưu dữ liệu

- Biến (variable) dùng để chứa dữ liệu.
- Tên biến:
	- là tổ hợp của các kí tự chữ cái, số và dấu gạch dưới \_.
	- phải bắt đầu bằng chữ cái hoặc dấu gạch dưới \_.
- Phép gán **=** dùng để đưa dữ liệu vào biến.
```Python
x = 5
name = input("Bạn tên là gì? ")
```
- Các kiểu dữ liệu (data types):
	- `int` : kiểu số nguyên, gồm các số nguyên. Ví dụ: 1, 2, 3, -1, -3, etc.
	- `float` : kiểu số thực, gồm các số thực. Ví dụ: 1.0, 2.0, 3.5, -1.5, etc.
	- `str` : kiểu chuỗi kí tự, gồm các chuỗi kí tự. Ví dụ: "2021", "1.5", "Bạn tên là gì? ", etc.
	- `bool`: kiểu logic, gồm 2 giá trị `True` (đúng) và `False` (sai).
- `type()` : dùng để kiểm tra kiểu dữ liệu
```Python
type(5)
# return <class 'int'>

name = "Bạn tên là gì? "
type(name)
# return <class 'str'>

type(True)
# return <class 'bool'>
```
- `int()` : dùng để chuyển dữ liệu dạng chuỗi kí tự (`str`), hoặc dạng logic (`bool`) sang dạng số nguyên (`int`). Lưu ý: nếu chuỗi đưa vào có chứa chữ cái hoặc dấu chấm `.`, hàm `int()` sẽ trả về lỗi `ValueError`.
```Python
int("20")
# return 20

int(True) # return 1
int(False) # return 0
```
- `str()` : dùng để chuyển dữ liệu dạng bất kì sang dạng chuỗi kí tự (`str`).
```Python
str(20)
# return '20'

str(20.5)
# return '20.5'

str(True)
# return 'True'
```
- `float()` : dùng để chuyển dữ liệu dạng chuỗi kí tự (`str`), hoặc dạng logic (`bool`) sang dạng số thực (`float`). Lưu ý: nếu chuỗi đưa vào có chứa chữ cái, hàm `float()` sẽ trả về lỗi `ValueError`.
```Python
float("20")
# return 20.0

float(True) # return 1.0
float(False) # return 0.0
```

## Câu điều kiện
- Cú pháp
```Python
if điều_kiện:
	mã_lệnh_nếu_điều_kiện_đúng
else:
	mã_lệnh_nếu_điều_kiện_sai
```
- Các phép toán so sánh:
	- **==**: bằng nhau. Kiểm tra 2 vế có giống nhau hay không?
	- **!=**: khác nhau. Kiểm tra 2 vế có khác nhau hay không?
	- **>**: lớn hơn. Vế trái lớn hơn vế phải?
	- **>=**: lớn hơn hoặc bằng. Vế trái lớn hơn hoặc bằng vế phải?
	- **<**: nhỏ hơn. Vế trái nhỏ hơn vế phải?
	- **<=**: nhỏ hơn hoặc bằng. Vế trái nhỏ hơn hoặc bằng vế phải?
- Các phép toán sẽ trả về dữ liệu kiểu logic (`bool`): `True` hoặc `False`.
```Python
type(3 > 4)
# return False
```
- Toán tử kết hợp `and` (và), `or` (hoặc): dùng để kết hợp nhiều điều kiện thành một.
```Python
# or
if x == "1101" or x == "1001":
	print("Welcome")
else:
	print("Wrong")

# and
if x > 3 and x < 8:
	print("Welcome")
else:
	print("Wrong")
```
- Rẽ nhánh
```Python
if điều_kiện_1:
	mã_lệnh_nếu_điều_kiện_1_đúng
elif điều_kiện_2:
	mã_lệnh_nếu_điều_kiện_2_đúng
else:
	mã_lệnh_nếu_điều_kiện_1_và_2_sai
```
- Trong câu điều kiện chỉ có thể có 1 `if`, có nhiều nhất 1 `else`, và có thể có vô số `elif`.
```Python
diem = input("Bạn được bao nhiêu điểm ? ")
diem = float(diem)
if diem >= 9:
	print("học sinh xuất sắc")
elif diem >=8:
	print("học sinh giỏi")
elif diem >= 6.5:
	print("học sinh khá")
else:
	print("học sinh trung bình")
```

## Vòng lặp