# Bài 4: Cỗ Máy Tìm Kiếm

> Thuật toán là một hướng dẫn **các bước cụ thể** để thực hiện một công việc nào đó.

- [x] [Tìm kiếm tuần tự (Linear Search)](#t%C3%ACm-ki%E1%BA%BFm-tu%E1%BA%A7n-t%E1%BB%B1-linear-search): ý tưởng, sơ đồ thuật toán, cài đặt
- [ ] Tìm kiếm nhị phân (Binary Search): ý tưởng, sơ đồ thuật toán, cài đặt
- [x] [Hàm (Function)](#h%C3%A0m-function): khái niệm, khai báo, sử dụng

## Tài nguyên

- [[Lesson 4] Common Mistake + Flashcard](https://docs.google.com/presentation/d/e/2PACX-1vSIVfGh1S7kVmT0uuCcCHh2HHbAsoOD9iC58-Hf8LZzmfHFyuvIdmi5DPoB1TGCtCmdusgs5RErVfgE/embed?start=false&loop=false&delayms=3000&slide=id.gb61af6f9ef_1_83)
- [[Lesson 4] Preparation slide](https://docs.google.com/presentation/d/e/2PACX-1vQ7merIUe4zP9PnNa9xuvlJq_DrgZUaQWKtYL2CxWkEu1VKsIOBgaQYA6NCdZvllfgwJH7AOR3j6gZN/embed?start=false&loop=false&delayms=3000&slide=id.gb4103d2256_3_320)
- [[Lesson 4] Final slide](https://docs.google.com/presentation/d/e/2PACX-1vRaplNGdh38_4pg7UMfNV0V2GGAHLpdnqvU4QhKbxFC6jaxTLAVKNIW1h4lccNsJK45WDL2I6dVvhX2/embed?start=false&loop=false&delayms=3000&slide=id.gb4103d2256_3_320)
- [[SUM 21] CS 101 - Thầy ơi, thầy đi đâu thế! (Phiên bản chưa sắp xếp)](https://scratch.mit.edu/projects/481099537/)
- [[SUM 21] CS 101 - Searching Algorithm simulation](https://scratch.mit.edu/projects/553779257)
- [[SUM 21] CS 101 - Lucky Luke selection sorting](https://scratch.mit.edu/projects/481274546/)
- [[SUM 21] CS 101 - Thầy ơi, thầy đi đâu thế! (Phiên bản sắp xếp)](https://scratch.mit.edu/projects/481099413/)
- [Khái niệm Thuật toán](https://www.powtoon.com/embed/dC5wiRKAnKf/)

## Tìm kiếm tuần tự (Linear Search)

### Ý tưởng
1. Đi qua từng phần tử trong mảng
2. ___ Nếu giá trị của phần tử hiện tại = giá trị cần tìm thì:
3. ______ In ra màn hình "đã tìm được". Đi đến bước 5.
4. In ra màn hình "không tìm được".
5. Kết thúc

### Sơ đồ thuật toán

1. Sử dụng vòng lặp `while`

![linear search using while](images/l4_linear_search_while.svg)

2. Sử dụng vòng lặp `for`

![linear search using for](images/l4_linear_search_for.svg)

### Cài đặt

1. Sử dụng vòng lặp `while`

```Python
found = False
index = 0
while index < len(mang):
    if mang[index] == so_can_tim:
        found = True
        print("found it")
        break
if found == False:
    print("not found")
```

2. Sử dụng vòng lặp `for`

```Python
found = False
for phan_tu in mang:
    if phan_tu == so_can_tim:
        found = True
        print("found it")
        break
if found == False:
    print("not found")
```

## Hàm (Function)

### Khái niệm

> Hàm là một khối lệnh được đặt tên (gọi là tên hàm) dùng để thực hiện một công việc nào đó.

- Hàm có thể có hoặc không yêu cầu các dữ liệu đầu vào (input). Dữ liệu được đưa vào hàm thông qua các biến. Các biến này được gọi làm **tham số** của hàm.

```Python
# hàm không yêu cầu tham số
def chao_chi():
    print("Hi Chi")

# hàm yêu cầu tham số
def chao(ten):
    print("Hi " + ten)
```

- Hàm có thể có hoặc không có dữ liệu trả về. Nếu có dữ liệu trả về nó được trả về thông qua câu lệnh `return`.

```Python
# hàm không có dữ liệu trả về
def chao_chi():
    print("Hi Chi")

# hàm có dữ liệu trả về
def chao_chi():
    return "Hi Chi"
```

### Khai báo

- Cú pháp:

```Python
def tên_hàm(các_tham_số_nếu_cần):
    lệnh_1
    lệnh_2
    ...
    lệnh_n
    return biến_hoặc_giá_trị_nếu_cần
```

- Quy tắc đặt tên hàm giống quy tắc đặt tên biến.
- Nếu hàm có nhiều tham số thì các tham số được cách nhau bởi dấu phẩy `,`
- Hàm sẽ dừng lại khi gặp lệnh `return`.  Do đó các lệnh đặt sau lệnh `return` sẽ không được thực hiện.
- Nếu hàm không có giá trị trả về nó sẽ trả về một giá trị đặc biệt là `None`.

> Nên sử dụng động từ để đặt tên cho hàm, danh từ để đặt tên cho biến.

Ví dụ dưới đây sẽ khai báo hàm `tinh_tong()` dùng để tính tổng của hai số.

```Python
def tinh_tong(a, b):
    tong = a + b
    return tong
```

### Sử dụng

Để sử dụng hàm ta chỉ cần gọi tên hàm và truyền vào các giá trị của tham số nếu có. Giá trị của tham số truyền vào được gọi là **đối số**.

Ví dụ để sử dụng hàm tính tổng ở trên để tính tổng của hai số 5 và 3 ta dùng câu lệnh `tinh_tong(5, 3)`.
- Câu lệnh này sẽ trả về 8 là tổng của 5 và 3.
- Nếu muốn lưu lại giá trị này ta cần sử dụng biến và phép gán: `tong = tinh_tong(5, 3)` .
- Nếu muốn in giá trị ra màn hình ta dùng hàm `print` như bình thường `print(tinh_tong(5, 3))`