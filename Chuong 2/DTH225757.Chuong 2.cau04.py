Câu 4: Python hỗ trợ những kiểu dữ liệu cơ bản nào ?
Các kiểu dữ liệu trong Python
-Kiểu dữ liệu số, Python hỗ trợ 4 kiểu dữ liệu số:
+ Kiểu int
+ Kiểu long
+ Kiểu float
+ Kiểu số phức (Complex)
-Kiểu dữ liệu Boolean
-Kiểu dữ liệu chuỗi 
-Kiểu dữ liệu phức, gồm: danh sách (list), bộ dữ liệu (tuple), từ điển (dictionary), tập hợp (set)

Câu 5: Các loại ghi chú trong Python
Python hỗ trợ 2 kiểu comment đó là comment 1 dòng và nhiều dòng. Trong Python, dấu # được dùng để comment đơn dòng. Tất cả các kí tự ở sau dấu # và kéo đến hết dòng thì được coi là một comment và được bỏ qua bởi trình thông dịch. Comment nhiều dòng nằm trong cặp 3 nháy.

Câu 6: Ý nghĩa toán tử /, //, %, **, and, or, is
-/  : Toán tử chia các giá trị cho nhau. Vd: 10 / 3 = 3.333333
-// : Toán tử chia lấy phần nguyên. Vd: 10 // 3 = 3
-%: Toán tử chia lấy phần dư. Vd: 10 % 3 = 1
-**: Tính lũy thừa. Vd: 2 ** 3 = 8
-And: Phép và. Nếu 2 điều kiện là True thì kết quả trả về True
-Or: Phép hoặc. Nếu 1 trong 2 điều kiện True thì kết quả trả về True
-Is: Trả về True nếu phần tử nằm trong 1 dãy phần tử. 

Câu 7: Trình bày một số cách nhập dữ liệu từ bàn phím
Python cung cấp hai hàm đã được xây dựng sẵn để nhận input từ người dùng là hàm
input() và hàm raw_input()

Câu 8: Trình bày các loại lỗi khi lập trình và cách bắt lỗi trong Python
-Lỗi cú pháp
-Lỗi thực thi
-Lỗi ngữ nghĩa

Câu 9: Giải thích kết quả tính toán của các biểu thức
Giá trị ban đầu:

i1 = 2
i2 = 5
i3 = -3
d1 = 2.0
d2 = 5.0
d3 = -0.5

Kết quả và giải thích: 

(a) i1 + (i2 * i3)
Kết quả: 2 + (5 * -3) = 2 - 15 = -13

(b) i1 * (i2 + i3)
Kết quả: 2 * (5 + -3) = 2 * 2 = 4

(c) i1 / (i2 + i3)
Kết quả: 2 / (5 + -3) = 2 / 2 = 1.0

(d) i1 // (i2 + i3)
Kết quả: 2 // (5 + -3) = 2 // 2 = 1

(e) i1 / i2 + i3
Kết quả: 2 / 5 + (-3) = 0.4 - 3 = -2.6

(f) i1 // i2 + i3
Kết quả: 2 // 5 + (-3) = 0 + (-3) = -3

(g) 3 + 4 + 5 / 3
Kết quả: 3 + 4 + (5 / 3) = 3 + 4 + 1.6667 ≈ 8.6667

(h) 3 + 4 + 5 // 3
Kết quả: 3 + 4 + (5 // 3) = 3 + 4 + 1 = 8

(i) (3 + 4 + 5) / 3
Kết quả: (3 + 4 + 5) / 3 = 12 / 3 = 4.0

(j) (3 + 4 + 5) // 3
Kết quả: (3 + 4 + 5) // 3 = 12 // 3 = 4

(k) d1 + (d2 * d3)
Kết quả: 2.0 + (5.0 * -0.5) = 2.0 - 2.5 = -0.5

(l) d1 + d2 * d3
Kết quả: 2.0 + 5.0 * -0.5 = 2.0 - 2.5 = -0.5

(m) d1 / d2 - d3
Kết quả: 2.0 / 5.0 - (-0.5) = 0.4 + 0.5 = 0.9

(n) d1 / (d2 - d3)
Kết quả: 2.0 / (5.0 - -0.5) = 2.0 / 5.5 ≈ 0.3636

(o) d1 + d2 + d3 / 3
Kết quả: 2.0 + 5.0 + (-0.5 / 3) = 2.0 + 5.0 - 0.1667 ≈ 6.8333

(p) (d1 + d2 + d3) / 3
Kết quả: (2.0 + 5.0 + -0.5) / 3 = 6.5 / 3 ≈ 2.1667

(q) d1 + d2 + (d3 / 3)
Kết quả: 2.0 + 5.0 + (-0.5 / 3) = 6.8333

(r) 3 * (d1 + d2) * (d1 - d3)
Kết quả: 3 * (2.0 + 5.0) * (2.0 - -0.5) = 3 * 7.0 * 2.5 = 52.5

Câu 10: Hãy viết ngắn gọn lại các lệnh dưới đây
(a) x = x + 1                   	 x += 1
(b) x = x / 2 			 x /= 2
(c) x = x – 1 		 x -= 1
(d) x = x + y 		 x += y
(e) x = x - (y + 7)		 x -= (y+7)
(f) x = 2*x			 x *= 2
(g) number_of_closed_cases = number_of_closed_cases + 2*ncc
 number_of_closed_cases += 2*ncc
