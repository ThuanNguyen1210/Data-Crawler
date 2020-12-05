# Data 
    Hai trong số những điều phổ biến hơn là:
    • Chính và Phụ: Dữ liệu chính là dữ liệu mà bạn thu thập hoặc tạo ra. 
      Dữ liệu thứ cấp được tạo ra bởi các nhà nghiên cứu khác và có thể là dữ liệu chính của họ hoặc dữ liệu kết quả 
      từ nghiên cứu của họ.
    • Định tính và Định lượng: Định tính đề cập đến văn bản, hình ảnh, video, bản ghi âm, quan sát, v.v. 
      Định lượng đề cập đến dữ liệu số.

# Phân loại data:
### Quan sát
    • Được chụp trong thời gian thực.
    • Không thể tái tạo hoặc lấy lại. Đôi khi được gọi là 'dữ liệu duy nhất'.
    • Ví dụ bao gồm chỉ số cảm biến, đo từ xa, kết quả khảo sát, hình ảnh và quan sát của con người.
### Thực nghiệm
    • Dữ liệu từ thiết bị phòng thí nghiệm và trong các điều kiện được kiểm soát.
    • Thường có thể tái tạo, nhưng có thể tốn kém để làm như vậy.
    • Ví dụ bao gồm trình tự gen, sắc ký đồ, đọc từ trường và quang phổ.
### Mô phỏng
    • Dữ liệu được tạo ra từ các mô hình thử nghiệm nghiên cứu các hệ thống thực tế hoặc lý thuyết.
    • Mô hình và siêu dữ liệu trong đó dữ liệu đầu vào quan trọng hơn dữ liệu đầu ra.
    • Ví dụ bao gồm các mô hình khí hậu, mô hình kinh tế và kỹ thuật hệ thống.
### Bắt nguồn hoặc biên dịch
    • Kết quả phân tích dữ liệu hoặc tổng hợp từ nhiều nguồn.
    • Có thể tái tạo (nhưng rất đắt).
    • Ví dụ bao gồm khai thác văn bản và dữ liệu, cơ sở dữ liệu được biên dịch và mô hình 3D.
### Tham chiếu hoặc chuẩn
    • Tập dữ liệu thu thập cố định hoặc không phải trả tiền, thường được đánh giá ngang hàng và thường được xuất bản và sắp xếp.
    • Ví dụ bao gồm cơ sở dữ liệu trình tự gen, dữ liệu điều tra dân số, cấu trúc hóa học.

### Định dạng tệp
    • Định dạng tệp nên được chọn để đảm bảo chia sẻ, truy cập lâu dài và bảo quản dữ liệu của bạn. 
    • Chọn các tiêu chuẩn và định dạng mở dễ sử dụng lại. 
    • Nếu bạn đang sử dụng một định dạng khác trong giai đoạn thu thập và phân tích nghiên cứu của mình, 
    hãy đảm bảo bao gồm thông tin  trong tài liệu của bạn về các tính năng có thể bị mất khi tệp được 
    chuyển sang định dạng bảo quản, cũng như bất kỳ phần mềm cụ thể nào sẽ cần thiết để xem hoặc làm việc với dữ liệu.

# JSON
• JavaScript Object Notation (JSON) là một giải pháp thay thế đang thu hút rất nhiều sự chú ý. 
Điều đầu tiên khi nhắc đến JSON với các nhà phát triển là được thiết kế nhẹ nhàng để có thể dễ dàng đọc trao đổi dữ liệu và thực thi. Tuy nhiên, đó không phải là lý do duy nhất bạn nên sử dụng JSON cho tích hợp API Restful.

• Các API RESTful phụ thuộc vào việc trao đổi dữ liệu dễ dàng, đáng tin cậy và nhanh chóng. 
    JSON phù hợp với hóa đơn cho từng thuộc tính này. Đây là lý do tại sao sử dụng ngôn ngữ này nhiều sẽ giúp bạn tạo ra các dịch vụ API thú vị.

• Mặc dù CSV là định dạng tệp phổ biến nhất cho dữ liệu “phẳng”, JSON là định dạng tệp phổ biến nhất cho dữ liệu “dạng cây” có khả năng có nhiều lớp, như các nhánh trên cây:

        {
        [
            {
                "id":0,
                "type":"chuối",
                "số lượng":12
            },
            {
                "id":1,
                "loại":"táo",
                "số lượng":7
            }
        ]
        }

• Đối với tệp JSON, bản xem trước tab Dữ liệu sẽ hiển thị một cây tương tác với các nút trong tệp JSON được đính kèm. 
Bạn có thể nhấp vào các phím riêng lẻ để mở và thu gọn các phần của cây, khám phá cấu trúc của tập dữ liệu khi bạn tiếp tục. 
Các tệp JSON không hỗ trợ mô tả hoặc chỉ số cột.

# Ưu điểm của JSON

1. JSON nhanh hơn - Cú pháp JSON rất dễ sử dụng. Chúng ta chỉ phải sử dụng như một cú pháp giúp chúng ta dễ dàng phân tích dữ liệu và thực thi dữ liệu nhanh hơn. Vì cú pháp của nó rất nhỏ và trọng lượng nhẹ, đó là lý do mà nó thực thi phản hồi theo cách nhanh hơn. Cách tiếp cận nhẹ của JSON có thể tạo ra những cải tiến đáng kể trong các API RESTful hoạt động với các hệ thống phức tạp.

2. Phân tích cú pháp máy chủ - Phân tích cú pháp phía máy chủ là phần quan trọng mà các nhà phát triển muốn nếu quá trình phân tích cú pháp sẽ nhanh ở phía máy chủ thì chỉ người dùng mới có thể nhận được phản hồi nhanh chóng của phản hồi của họ vì vậy trong trường hợp này phân tích cú pháp phía máy chủ JSON là điểm mạnh mà cho biết chúng tôi sử dụng JSON ở phía máy chủ.

3. Hỗ trợ lược đồ - Nó có nhiều loại trình duyệt được hỗ trợ tương thích với các hệ điều hành, vì vậy các ứng dụng được tạo bằng mã hóa JSON không đòi hỏi nhiều nỗ lực để làm cho nó tương thích với tất cả các trình duyệt. Trong quá trình phát triển, nhà phát triển nghĩ cho các trình duyệt khác nhau nhưng JSON cung cấp chức năng đó.

4. Công cụ chia sẻ dữ liệu - JSON là công cụ tốt nhất để chia sẻ dữ liệu ở bất kỳ kích thước nào kể cả âm thanh, video, v.v. Điều này là do JSON lưu trữ dữ liệu trong các mảng nên việc truyền dữ liệu dễ dàng hơn. Vì lý do này, JSON là một định dạng tệp cao cấp cho các API web và để phát triển web.




