# Đăng TikTok từ MathTuber

Nghiên cứu ngày 05/09/2026. Chưa đăng nhập hoặc upload thử TikTok trong phiên này.

## Kết luận

Với kênh cá nhân hiện tại, nên bắt đầu bằng **TikTok Studio trên web**. MathTuber xuất MP4 dọc có phụ đề, ảnh cover và caption; người dùng đăng nhập tài khoản TikTok rồi upload. Có thể thử hỗ trợ thao tác bằng browser tool của host, nhưng mức tự động hóa phụ thuộc giao diện, công cụ chọn file, phiên đăng nhập và các bước xác thực thực tế. Đây chưa phải adapter đã chạy thử.

TikTok có hai API chính thức, nhưng không thể coi token là đủ để tự động đăng công khai. YouTube OAuth không dùng được cho TikTok.

| Cách đăng | Điều kiện | Kết thúc luồng |
|---|---|---|
| TikTok Studio web | Tài khoản TikTok và phiên đăng nhập | Xem preview, chọn thông tin và đăng trên giao diện TikTok |
| Content Posting API — Upload | App được duyệt scope `video.upload`, người dùng cấp OAuth | Gửi vào inbox; người dùng mở TikTok để chỉnh và hoàn tất bài đăng |
| Content Posting API — Direct Post | App được duyệt scope `video.publish`; audit để bỏ giới hạn riêng tư | API gửi video, theo dõi xử lý và trả trạng thái bài đăng |

Nguồn: [TikTok Studio](https://support.tiktok.com/en/using-tiktok/creating-videos/tiktok-studio), [Upload prerequisites](https://developers.tiktok.com/docs/en/content-posting-api-get-started-upload-content), [Direct Post prerequisites](https://developers.tiktok.com/docs/en/content-posting-api-get-started).

## Giới hạn quan trọng của Direct Post

TikTok quy định app chưa audit chỉ được đăng `SELF_ONLY`, tối đa 5 người dùng trong 24 giờ, và các tài khoản đó phải để private khi đăng. Hướng dẫn cũng loại trừ utility chỉ phục vụ tài khoản của chính người phát triển/nhóm; app phải phục vụ nhóm người dùng rộng hơn. Vì vậy không nên lập một app nội bộ rồi kỳ vọng tự động được duyệt để đăng public. Một sản phẩm MathTuber thực sự phục vụ nhiều creator có thể là hướng dài hạn, nhưng quyết định duyệt thuộc TikTok.

UX Direct Post cần hiện đúng tài khoản, preview và lựa chọn người dùng: privacy không có giá trị mặc định; quyền tương tác phải theo creator info; title/hashtag được sửa; có lựa chọn khai báo thương mại và đồng ý trước khi gửi. Một JSON `authorized: true` đơn độc không thay thế đầy đủ UX này.

Nguồn: [Content Sharing Guidelines](https://developers.tiktok.com/docs/en/content-sharing-guidelines), cập nhật 04/08/2026.

## Thiết kế adapter nếu triển khai

1. OAuth TikTok riêng; giữ client secret và refresh token ngoài repo. Không tái sử dụng Google token hay trích cookie từ trình duyệt.
2. Với Direct Post, gọi `creator_info/query` trước để lấy giới hạn thời lượng và privacy được phép; hiển thị cho người dùng trên một trang preview cục bộ.
3. Video nằm trên máy nên dùng `FILE_UPLOAD`. API khởi tạo trả `publish_id` và `upload_url`; ghi receipt trước khi gửi các chunk. `PULL_FROM_URL` chỉ phù hợp khi có domain/prefix đã xác minh. Không cần dựng dịch vụ lưu trữ video chỉ để upload file local.
4. Direct Post dùng `/v2/post/publish/video/init/`; inbox dùng `/v2/post/publish/inbox/video/init/`. Giữ chúng thành hai hành động khác nhau, không gọi inbox delivery là đã đăng.
5. Poll trạng thái theo `publish_id`. `SEND_TO_USER_INBOX` nghĩa là người dùng còn phải hoàn tất; `PUBLISH_COMPLETE` mới là đã đăng. Sau lỗi không rõ kết quả, đối soát receipt trước khi tạo upload mới.
6. Direct Post hỗ trợ cover timestamp và `is_aigc`. MathTuber có giọng tổng hợp nên cần cung cấp lựa chọn khai báo AI rõ ràng; không tự gắn nhãn sai về người thật hay nội dung thương mại.

Nguồn: [Direct Post reference](https://developers.tiktok.com/doc/content-posting-api-reference-direct-post), [Media Transfer Guide](https://developers.tiktok.com/docs/en/content-posting-api-media-transfer-guide), [Upload reference](https://developers.tiktok.com/docs/en/content-posting-api-reference-upload-video), [Post status](https://developers.tiktok.com/docs/en/content-posting-api-reference-get-video-status).

## Cách dùng ngay

Mở [TikTok Studio](https://www.tiktok.com/tiktokstudio), đăng nhập tài khoản TikTok cần đăng, chọn Upload và chọn bản MP4 có phụ đề. Xem lại preview, sửa caption, chọn cover, kiểm tra khai báo AI, chọn người được xem và đăng. Lưu link bài đăng sau khi TikTok xử lý xong. Tên/vị trí nút có thể thay đổi theo phiên bản và tài khoản; chưa kiểm tra giao diện đăng nhập thực tế ở đây.

Cho MathTuber: triển khai bộ xuất `video.mp4 + cover.jpg + caption.txt + receipt.json` trước; thêm workflow browser theo khả năng host; chỉ xây Direct Post sau khi xác định app và UX có đường được duyệt. API inbox vẫn cần scope được duyệt, không phải đường miễn đăng ký hoặc miễn xét duyệt.
