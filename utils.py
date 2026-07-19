import pandas as pd
from dbnomics import fetch_series

def fetch_imf_data(country_dict, dataset_code="IFS", metric_suffix="PCPI_IX", frequency="M"):
    """Fetch macroeconomic data from the IMF via DBnomics with dynamic dataset mapping.

    Parameters:
    -----------
    country_dict : dict
        A dictionary containing country codes (keys) and display names (values).
    dataset_code : str
        The IMF dataset code on DBnomics. 'CPI' for inflation only, 'IFS' for general macro data.
    metric_suffix : str
        The specific IMF metric code (e.g., 'NGDP_R_XDC', 'LUR_P_PE_NUM').
    frequency : str
        Data frequency: 'M' (Monthly), 'Q' (Quarterly), 'A' (Annual).
    """
    all_dfs = []

    for code, country_name in country_dict.items():
        # Tạo endpoint chính xác dựa trên dataset_code
        series_id = f"IMF/{dataset_code}/{frequency}.{code}.{metric_suffix}"

        try:
            df = fetch_series(series_id)
            df["country_name"] = country_name
            df["country_code"] = code
            all_dfs.append(df)
        except Exception as e:
            # Nếu chạy IFS bị lỗi (một số nước nộp dữ liệu trễ), hệ thống sẽ log ra để kiểm tra
            print(f"Error {country_name} ({series_id}): {e}")

    if all_dfs:
        
        return pd.concat(all_dfs, ignore_index=True)
    else:
        print("No data was successfully loaded.")
        return pd.DataFrame()
    

def fetch_imf_bulk(dataset_code="IFS", metric_code="NGDP_R_XDC", frequency="Q", country_list=None):
    """
    Cào dữ liệu vĩ mô từ IMF bằng phương pháp lọc Dimension của DBnomics.
    Tránh lỗi nối chuỗi ID sai cấu trúc.
    """
    print(f"--- Đang tải dữ liệu cho mã: {metric_code} ({frequency}) ---")
    
    # Thiết lập bộ lọc kích thước (Dimensions) theo chuẩn API DBnomics
    # FREQ: Tần suất (M, Q, A)
    # INDICATOR: Mã chỉ số vĩ mô của IMF
    if dataset_code=="WEO:2025-04" and metric_code=="LUR":
        dimensions = {
            # "freq": [frequency],
            "weo-subject": [metric_code],
            "unit": 'pcent'
        }
        
        # Nếu người dùng truyền vào danh sách mã nước cụ thể (ví dụ: ['VN', 'US', 'DE'])
        if country_list:
            dimensions["weo-country"] = country_list
    else:
        dimensions = {
            "FREQ": [frequency],
            "INDICATOR": [metric_code]
        }
        
        # Nếu người dùng truyền vào danh sách mã nước cụ thể (ví dụ: ['VN', 'US', 'DE'])
        if country_list:
            dimensions["REF_AREA"] = country_list

    try:
        # Gọi API tải hàng loạt theo bộ lọc
        df = fetch_series(provider_code="IMF", dataset_code=dataset_code, dimensions=dimensions)
        
        if df.empty:
            print(f"⚠️ Không tìm thấy dữ liệu nào khớp với mã {metric_code}.")
            return pd.DataFrame()
            
        # Chuẩn hóa lại tên cột để đồng bộ với cấu trúc Power BI của bạn
        # DBnomics trả về cột 'REF_AREA' làm mã quốc gia và 'Reference Area' làm tên quốc gia
        df = df.rename(columns={
            "REF_AREA": "country_code",
            "Reference Area": "country_name",
            "period": "Date"
        })
        
        # Chỉ giữ lại các cột cốt lõi cần thiết cho Dashboard
        core_columns = ["Date", "value", "country_code", "country_name"]
        df = df[[col for col in core_columns if col in df.columns]]
        
        print(f"✅ Tải thành công {len(df)} dòng dữ liệu!")
        return df

    except Exception as e:
        print(f"❌ Lỗi hệ thống khi gọi API: {e}")
        return pd.DataFrame()