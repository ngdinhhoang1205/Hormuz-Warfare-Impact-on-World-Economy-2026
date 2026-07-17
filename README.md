Phân tích tác động của việc phong tỏa Eo biển Hormuz đối với kinh tế toàn cầu từ đầu năm 2026

Key metrics:
- Inflation
- Brent & WTI price
- LNG Spot Price
- Drewry World Container Index hoặc Baltic Dry Index
- Policy Interest Rates


Data sources:
A. Dữ liệu Lạm phát (CPI) và Vĩ mô theo Quốc gia/Khu vựcIMF và World Bank API (Python wbgapi hoặc pandas-datareader):Nội dung: Cung cấp dữ liệu CPI lịch sử theo tháng của hầu hết các quốc gia trên thế giới.Cách dùng: Bạn có thể viết code Python gọi trực tiếp API của World Bank để lấy chỉ số CPI từ năm 2020 đến nay cho các nhóm nước thuộc Đông Nam Á (ASEAN), Châu Âu (Eurozone), v.v.DBnomics (db.nomics.world):Nội dung: Một nền tảng mở tuyệt vời tổng hợp dữ liệu kinh tế từ tất cả các nhà cung cấp lớn (Eurostat, IMF, OECD, World Bank). Họ có thư viện Python (dbnomics) để bạn tải trực tiếp các chuỗi thời gian CPI về máy.
wbgapi
dbnomics
B. Dữ liệu Giá Năng lượng và Hàng hóaYahoo Finance API (Thư viện Python yfinance):Nội dung: Dữ liệu lịch sử giá dầu Brent (BZ=F), dầu WTI (CL=F), và khí gas tự nhiên (NG=F) theo ngày/giờ.  Ưu điểm: Cực kỳ sạch, cập nhật liên tục đến ngày hôm nay và hoàn toàn miễn phí.Kaggle Datasets:Tìm kiếm các keyword: "Global Inflation Dataset", "Crude Oil Prices Daily Update", hoặc "Commodity Prices World Bank". Thường có các bộ dữ liệu được cập nhật tự động hàng tuần bằng GitHub Actions từ các nguồn uy tín.
C. Dữ liệu Vận tải biển & LogisticsFederal Reserve Bank of St. Louis (FRED API):Nội dung: Ngân hàng Dự trữ Liên bang St. Louis cung cấp kho dữ liệu vĩ mô FRED khổng lồ.Chỉ số nên lấy: Chỉ số Áp lực Chuỗi Cung ứng Toàn cầu (GSCPI - Global Supply Chain Pressure Index) hoặc giá cước container chuyên chở. Bạn có thể dùng thư viện fredapi trong Python để kết nối trực tiếp.