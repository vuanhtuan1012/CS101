# Bài 8: Khám Phá Thế Giới Đối Tượng

- [x] Lập trình hướng đối tượng (object-oriented programming).
- [x] Lớp (class): khái niệm, khai báo lớp, thuộc tính (attribute), phương thức (method), phân biệt phương thức và hàm.

## Tài nguyên

- [[Lesson 8]  Common Mistakes + Flashcard](https://docs.google.com/presentation/d/e/2PACX-1vTybbBDHDUKRbiDYQAiWyPCNRSsXcGH1S7YKekeXMjc0ZinikOXVPod2uucvsPpM1Lvaw7fZXRwPMjZ/embed?start=false&loop=false&delayms=3000&slide=id.gb61af6f9ef_1_83)
- [[Lesson 8] Preparation slide](https://docs.google.com/presentation/d/e/2PACX-1vTORGZ9F83o43EuKtSKjDraHQaFSVJSq3CJCYZZkqieA2u91TYzsZ1N6Q84tPtc3eJZ2qNSrr4TDr1D/embed?start=false&loop=false&delayms=3000&slide=id.p)
- [[Lesson 8] Final slide](https://docs.google.com/presentation/d/e/2PACX-1vQZ1ydtZysS6fdX9Pi3szSIk9fwyeo2Q7GPi9yQW_f6Yi3jDhXEfqW-C7-YjRJn12ioiAz4Tlm6xk5a/embed?start=false&loop=false&delayms=3000&slide=id.p)
- [[SUM 21] CS 101 - Lesson 8](https://scratch.mit.edu/projects/557621944/)
- [[Lesson 8] Tóm tắt nội dung bài học](https://www.youtube.com/watch?v=rYE5pKW47HQ)
- [[Lesson 8] Game](L8_Game.zip)

## Lập trình hướng đối tượng (Object-Oriented Programming)

> Lập trình hướng đối tượng (Object-Oriented Programming) là cách chia nhỏ chương trình thành các **đối tượng** (object) có các **đặc điểm** và **hành động**.

> Một **đối tượng** bao gồm các **đặc điểm** (thuộc tính, attribute) và **hành động** (phương thức, method).

## Lớp (Class)

- **Lớp** (class) là một **bản vẽ thiết kế** để **tạo ra các đối tượng** (object).
- Lớp sẽ cho biết đối tượng có các **thuộc tính** (attribute) và **phương thức** (method) nào.
- Các đối tượng được tạo ra từ cùng một lớp là các vật **riêng biệt**. Do đó, thuộc tính của chúng có thể mang các giá trị khác nhau.

### Khai báo một lớp trong Python

```Python
class Tên_Lớp:
    def __init__(self, tham_số_1, tham_số_n):
        self.thuộc_tính_1 = tham_số_1
        self.thuộc_tính_n = tham_số_n
```
Trong đó:
- `self` là từ khoá đặc biệt dùng để tham chiếu đến đối tượng mình đang tạo ra.
- `__init__` là tên hàm đặc biệt dùng để khởi tạo đối tượng.
- Các thuộc tính (nếu có) của lớp luôn được khởi tạo trong hàm `__init__`.

Ví dụ dưới đây khai báo lớp `Player` có hai thuộc tính `x`, `y`. Sau đó khởi tạo 2 đối tượng `nc1` và `nc2` thuộc lớp `Player`.

```Python
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
nc1 = Player(20, 30)
nc2 = Player(30, 50)
```

### Truy cập thuộc tính

> Để truy cập thuộc tính của đối tượng, ta sử dụng dấu chấm `.`: `tên_đối_tượng.tên_thuộc_tính`.

```Python
print(nc1.x)  # 20
print(nc2.x)  # 30
```

### Khai báo phương thức

Tương tự như tạo hàm, để khai báo một phương thức ta sử dụng từ khoá `def`. Cú pháp như sau:

```Python
def tên_phương_thức(self, tham_số_1, tham_số_n):
    các câu lệnh trong phương thức
```

Trong đó:
- `self` là từ khoá đặc biệt dùng để truy cập đến đối tượng đang tạo ra.
- Giống như hàm, phương thức cũng có thể có giá trị trả về, hoặc không. Nếu có, từ khoá `return` cũng được sử dụng để trả về giá trị của phương thức.

Ví dụ dưới đây sẽ khai báo phương thức `move()` dùng để di chuyển đối tượng sang phải 10 bước.

```Python
def move(self):
    self.x += 10
```

> Giống như truy cập thuộc tính, ta cũng dùng dấu chấm `.` để **gọi phương thức**: `tên_đối_tượng.tên_phương_thức()`

**!!! Chú ý !!!**
- Phương thức thuộc lớp, nên nó **phải được khai báo bên trong lớp**.
- Phương thức **phải có** tham số `self`. Tham số này luôn được **đặt ở vị trí đầu tiên**.
- Giống như trong hàm, tham số trong phương thức có thể nhận mọi kiểu dữ liệu, kể cả là một đối tượng.

### Phân biệt phương thức và hàm

- Phương thức khai báo bên trong lớp. Hàm khai báo ngoài lớp.
- Phương thức có tham số đặc biệt `self`. Hàm không có tham số `self`.