Đề tài: Thu thập thông tin tuyển dụng từ trang web chotot.vn

Công cụ: 
- Sử dụng thư viện beautifulsoup của python để làm web-spider
- Sử dụng json file để lưu kết quả crawler được

Để chạy web crawler
Open terminal > run command: python crawler.py

Cơ chế hoạt động:
- Beautifulsoup sẽ request đến trang web để lấy được source HTML code
- Các trường thông tin được lưu trong các tag với các class nhất định, lợi dụng điều đó ta dùng method find với tag và class để truy xuất đến từng link tuyển dụng
- Sử dụng beautifulsoup lần nữa để lấy được source HTML code của trang web mới
- Tìm các trường dữ liệu trong các tag tương ứng và xử lý chúng.
- Dữ liệu thông tin tuyển dụng trả về được lưu dưới dạng một list các dict của python (gồm các key và value)
- Viết dữ liệu thu được vào file JSON

Tiêu chí khi crawl dữ liệu về:
- Có ít nhất 11 trường thông tin {'Tiêu đề tuyển dụng','Hình thức trả lương','Loại công việc','Ngành nghề','Kinh nghiệm','Giới tính','Tên công ty','Số lượng',
                                  'Tuổi tối thiểu','Tuổi tối đa','Địa chỉ'}. Tùy tin tuyển dụng sẽ có thêm 2 trường mới là {'Quyền lợi','Học vấn tổi thiểu'}
- Thông tin được mã hóa dạng utf-8      
                            
Cài đặt
- Open terminal >
  + pip install requests
  + pip install html5lib
  + pip install bs4
  
TODO
- Triển khai việc: Crawl dữ liệu, xây dựng Bộ dataset (~ 10.000.)
- Cải tiến công cụ (source code đã xây dựng) để tạo thành công cụ hoàn chỉnh cho việc Crawl dữ liệu (sử dụng cho web không public API, yêu cầu đăng nhập, dùng js load động, ...) 
- Tìm hiểu cách làm sạch, chuẩn hóa dữ liệu, phân loại dữ liệu. 
- Thiết kế CLDS, các định dạng file biểu diễn dataset. 
- Kết quả dự kiến: dataset, bản thiết kế CSDL, báo cáo tìm hiểu về cách làm sạch, source code nếu có.
