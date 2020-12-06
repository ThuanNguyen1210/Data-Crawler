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

# Dataset
    Dataset của nhóm có định dạng file JSON gồm các field:
    job_title, company, salary, location, position, job_description, job_requirement, benefit, quantity
    
    [
    {
        "job_title": "Chuyên Viên Kinh Doanh - Hỗ Trợ Có Giao Dịch Sau 3 Tuần (Hh 80-100Tr)",
        "company": "Công ty CP bất động sản Highland Việt Nam",
        "salary": "Trên 30 triệu",
        "location": "Hà Nội",
        "position": "Nhân viên",
        "job_description": "Nắm vững các thông tin về những dự án công ty đang triển khai, phân phối', 'Duy trì và chăm sóc khách hàng hiện hữu.', 'Tư vấn trực tiếp khách hàng những sản phẩm của công ty dựa trên data có sẵn, hoặc data tiềm năng từ khai thác các kênh marketing.', 'Giới thiệu, hướng dẫn khách hàng tham quan nhà mẫu và các dự án do Công ty phân phối.', 'Thực hiện giao dịch, ký kết hợp đồng mua bán cũng như hỗ trợ khách hàng theo dõi tiến độ thanh toán",
        "job_requirement": "Nam / Nữ từ 22 - 30tuổi.', 'Không yêu cầu kinh nghiệm (Sẽ được đào tạo bài bản nếu trúng tuyển).', 'Có laptop và phương tiện đi lại.', 'Có khả năng giao tiếp, trình bày, thuyết phục tốt', 'Có khả năng học hỏi nhanh, nhiệt tình với công việc, chịu được áp lực cao trong công việc', 'Muốn phát triển bản thân, đột phá thu nhập', 'Ưu tiên ứng viên có kinh nghiệm bán hàng tư vấn các lĩnh vực tài chính, bảo hiểm, ô tô, hoặc đã từng làm trong lĩnh vực BĐS",
        "benefit": "LƯƠNG THƯỞNG HẤP DẪN: Lương cứng + 70% hoa hồng (hoa hồng từ 50-100tr/sp),', 'Hỗ trợ Marketing không giới hạn, Được hỗ trợ data khách hàng khi mới bắt đầu công việc', 'Làm việc trong môi trường chuyên nghiệp và năng động, chủ động trong thời gian làm việc, có cơ hội được học tập và phát triển bản thân', 'Cơ hội thăng tiến ca', 'Được đào tạo bài bản từ cơ bản đến chuyên sâu', 'Đào tạo ứng dụng Marketing và các kênh tìm kiếm khách hàng', 'Đào tạo các kỹ năng cần thiết: bán hàng, giao tiếp, làm việc nhóm,…', 'Được sự hỗ trợ của các Leader có kinh nghiệm trong lĩnh vực BĐS', 'Trở thành nhân viên phân phối các sản phẩm BĐS hot nhất thị trường', 'Tham gia các hoạt động nội bộ có một không hai mang đậm dấu ấn HIGHLAND trong năm: Year-End Party, Teambuilding, Giáng Sinh, Sinh nhật….', 'Được tham gia đi du lịch cùng công ty 1 lần/năm', 'Được hưởng Các chế độ phúc lợi: Thưởng, Nghỉ lễ, Tết và được tham gia BHXH.', 'Chế độ khen thưởng hấp dẫn theo Tháng, Quý, Năm,…', 'Được hưởng lương tháng 13",
        "quantity": "5"
    }
    ]

