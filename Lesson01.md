# Bài 1: Siêu Máy Tính
- [x] Số nhị phân
- [x] Emoji
- [x] Giới thiệu về Python

## Tài nguyên

- Slide: [[Lesson 1] Final slide - Google Slides](https://docs.google.com/presentation/d/e/2PACX-1vSwCVVx54yw5HrxqYj_-6y70_fqsqqa385gr_fFpH09dbnjx10i2eqoMtMBZrhFItXb8U6pDytEzYgr/embed?start=false&loop=false&delayms=3000&slide=id.p)
- Hướng dẫn cài Thonny: [CS101_Thonny Installation_LMS](https://docs.google.com/document/d/e/2PACX-1vShSM83TtpgfeImrq5u6O9ZImebCfVi92YapPaVdkBRJyXpzjUAWN-R4gct1tQlhS1CVDn0fOSpeAlm/pub?embedded=false)
- Flashcard [[Lesson 1] Common Mistake + Flashcard - Google Slides](https://docs.google.com/presentation/d/e/2PACX-1vTJqkJPXThCRTVx3JtgthdF0F8XR01SpqWjllIlUSh3o48Gt7vrFY8DCtX6twJFpHzdlgjy_INS9q6u/embed?start=false&slide=id.gb2c15e966d_0_0)
- Python IDE online: [Python Online Compiler & Interpreter - Replit](https://replit.com/languages/python3)
- Binary Light Bulbs: https://scratch.mit.edu/projects/446851585/

## Số nhị phân

### Khái niệm
- Con người đếm: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 (hệ thập phân)
- Máy tính đếm: 0, 1 (hệ nhị phân)

### Biểu diễn
- Hệ thập phân: 357 = 3x10^2  +  5x10^1 + 7x10^0
- Hệ nhị phân: 110_2 = 1x2^2 + 1x2^1 + 0x2^0

### Các hàm Python

- `ord()`: trả về mã unicode của 1 kí tự bất kì
	- input: 1 kí tự
	- output: mã unicode của kí tự đó
```Python
ord('A')
# return 65
```

- `char()`: trả về kí tự của mã unicode
	- input: 1 số nguyên
	- output: kí tự unicode
```Python
chr(65)
# return 'A'
```

- `bin()`: chuyển một số nguyên sang hệ cơ số 2
	- input: 1 số nguyên
	- output: biểu diễn của số nguyên đó trong hệ cơ số 2
```Python
bin(7)
# return '0b111'

"""
- 0b: cho biết đây là biểu diễn trong hệ nhị phân (cơ số 2)
- 111: biểu diễn của số 7 trong hệ nhị phân
"""
```

- `int()`: chuyển một chuỗi từ hệ nhị phân (cơ số 2) sang hệ thập phân (cơ số 10)
	- input: cần 2 giá trị: chuỗi cần chuyển và hệ cơ số của chuỗi đó
	- output: số nguyên trong hệ thập phân
```Python
int('111', 2)
# return 7

"""
- '111': chuỗi chứa số trong hệ nhị phân (cơ số 2)
- 2: báo cho hàm `int()` biết chuỗi này ở hệ nhị phân
"""
```