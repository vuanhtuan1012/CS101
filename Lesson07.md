# Bài 7: Giải Mã Mê Cung

- [x] Tìm kiếm theo chiều sâu (DFS)
- [ ] Cấu trúc dữ liệu: 
	- [x] Ngăn xếp (stack)
	- [x] Hàng đợi (queue)
	- [ ] Từ điển (dictionary)
- [ ] Tìm kiếm theo chiều rộng (BFS)

## Tài nguyên

- [[Lesson 7] Common Mistake + Flashcard](https://docs.google.com/presentation/d/e/2PACX-1vQzxayWSYlusJKF4ck20bldTH9PcOfFLBWY6mOBE8HvHdeKjDgaxbIsKHifoc2rNBEsLBS8k8IU0zB2/embed?start=false&loop=false&delayms=3000&slide=id.gb61af6f9ef_1_83)
- [[Lesson 7] Preparation slide](https://docs.google.com/presentation/d/e/2PACX-1vRoUpxp3llaul9tO4Q-q-8RKdUJ5e1m604B1amMwKLEwXnBvrwYEksqP9K8nDMxkE1PlIH96AVTugjg/embed?start=false&loop=false&delayms=3000&slide=id.ge5d5a056b8_0_0)
- [[Lesson 7] Final slide](https://docs.google.com/presentation/d/e/2PACX-1vRewSXmND2fH9BRe1t1W4hJmW2o8lIU-HLOSwwwyIQhRun3rLFHbYSoFieEXfiqRPaLmdPnsUz1YjQ-/embed?start=false&loop=false&delayms=3000&slide=id.gc1c2dc763d_1_0)
- [[SUM 21] CS101 - Trẩu và Tre ở sân bay](https://scratch.mit.edu/projects/556876796/)
- [[SUM 21] CS101 - Giải mã mê cung manual](https://scratch.mit.edu/projects/493904924/)
- [[SUM 21] CS101 - Giải mã mê cung](https://scratch.mit.edu/projects/493741831/)
- [[Lesson 7] Hướng dẫn cài đặt Pygame trên Thonny](https://www.youtube.com/watch?v=fSvHeLfE9yY)
- [[Lesson 7] Tóm tắt nội dung bài học](https://www.youtube.com/watch?v=ICsYgywXVwA)

## 1. Tìm kiếm theo chiều sâu (Depth First Search)

**Bài toán:** Chúng ta cần tìm đường đi **từ lối vào đến lối ra** của một mê cung như hình dưới.
![Maze](images/maze.jpg)

**Ý tưởng:**
1. Chúng ta đi theo một nhánh cho đến khi tìm được đường ra hoặc hết đường.
2. Nếu hết đường thì quay lại cho đến khi gặp nhánh mới, sau đó quay lại bước 1.

(xem [slide 22](https://docs.google.com/presentation/d/e/2PACX-1vRewSXmND2fH9BRe1t1W4hJmW2o8lIU-HLOSwwwyIQhRun3rLFHbYSoFieEXfiqRPaLmdPnsUz1YjQ-/embed?start=false&loop=false&delayms=3000&slide=id.gc1079d7cf4_0_18))

**Thuật toán DFS:**
1. Đến điểm xuất phát.
2. Đánh số vị trí hiện tại. *(Các vị trí khác nhau sẽ được đánh số bởi các số khác nhau.)*
3. Nhìn xung quanh theo thứ tự **trên - dưới - trái - phải** xem có **đường chưa đánh dấu** không?
	- Nếu có, sang bước 4.
	- Nếu không, sang bước 5.
4. Đi sang ô tiếp theo, ghi lại số của ô vừa đứng vào hộp `đã-đi-qua`. Sau đó, quay lại bước 2.
5. Lấy **số trên cùng** trong hộp `đã-đi-qua`, quay lại vị trí trong số đó. Sau đó, thực hiện bước 3.

**Nhận xét:** Nếu mê cung có lối ra, thuật toán DFS sẽ **luôn tìm được** lối ra.

## 2. Cấu trúc dữ liệu

### 2.1. Ngăn xếp (Stack)

**Khái niệm:**
- Ngăn xếp là một cấu trúc dữ liệu theo nguyên tắc thiết kế **vào sau ra trước** (Last In First Out - **LIFO**).
- Ngăn xếp có hai thao tác chính:
	- thêm phần tử vào ngăn xếp *(ở vị trí trên cùng)*, gọi là **push**.
	- lấy phần tử *(ở vị trí trên cùng)* ra khỏi ngăn xếp, gọi là **pop**.

(xem [slide 84](https://docs.google.com/presentation/d/e/2PACX-1vRewSXmND2fH9BRe1t1W4hJmW2o8lIU-HLOSwwwyIQhRun3rLFHbYSoFieEXfiqRPaLmdPnsUz1YjQ-/embed?start=false&loop=false&delayms=3000&slide=id.gbfd97ff75c_0_15))

**Lập trình:**
- Khởi tạo ngăn xếp: `stack = []`
- Thêm phần tử `item` vào ngăn xếp (**push**): `stack.append(item)`
- Lấy phần tử *(ở vị trí trên cùng)* ra khỏi ngăn xếp (**pop**): `item = stack.pop()`

### 2.2. Hàng đợi (Queue)

**Khái niệm:**
- Hàng đợi là một cấu trúc dữ liệu theo nguyên tắc thiết kế **vào trước ra trước** (First In First Out - **FIFO**)
- Hàng đợi có hai thao tác chính:
	- thêm phần tử vào hàng đợi (ở vị trí sau cùng), gọi là **enqueue**.
	- lấy phần tử (ở vị trí đầu tiên) ra khỏi hàng đợi, gọi là **dequeue**.

(xem [slide 110](https://docs.google.com/presentation/d/e/2PACX-1vRewSXmND2fH9BRe1t1W4hJmW2o8lIU-HLOSwwwyIQhRun3rLFHbYSoFieEXfiqRPaLmdPnsUz1YjQ-/embed?start=false&loop=false&delayms=3000&slide=id.gb840d41073_3_122))

**Lập trình:**
- Khởi tạo hàng đợi: `queue = []`
- Thêm phần tử `item` vào hàng đợi (**enqueue**): `queue.append(item)`
- Lấy phần tử *(ở vị trí đầu tiên)* ra khỏi hàng đợi (**dequeue**): `item = queue.pop(0)`