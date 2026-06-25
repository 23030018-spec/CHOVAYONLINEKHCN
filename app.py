STV=float(input("NHẬP SỐ TIỀN MUỐN VAY (TRIỆU ĐỒNG):"))
TGV=float(input("NNHẬP THỜI GIAN VAY (SỐ NĂM):"))
LSV=float(input("NHẬP LÃI SUẤT CHO VAY (SỐ THẬP PHÂN:"))
TN=float(input("NHẬP THU NHẬP HÀNG THÁNG (TRIỆU ĐỒNG/THÁNG):"))
SNTGD=float(input("NHẬP NGƯỜI TRONG GIA ĐÌNH (SỐ NGƯỜI):"))
CPSH=5
PTMC=float(input("NHẬP SỐ TIỀN PHẢI TRẢ CHO KHOÀN VAY CŨ (TRIỆU ĐỒNG):"))
PTMM=(STV/(TGV*12))+(STV*(LSV/12))
DTI=(PTMC+PTMM)/(TN-SNTGD*CPSH)
GTTSDB=float(input("NHẬP GIÁ TRỊ TSDB (TRIỆU ĐỒNG):"))
LTV=STV/GTTSDB
STKKH=float(input("NHẬP SỐ TUỔI KHÁCH HÀNG (TUỔI):"))
print(f"Chỉ số DTI là:{DTI*100}%")
print(f"Chỉ số LTV là:{LTV*100}%")
if DTI<=0.7 and LTV<=0.7 and 18<=STKKH<=70:
  print("ĐƯỢC CHO VAY")
else:
  print("KHÔNG ĐƯỢC CHO VAY")
  import streamlit as st

st.title("Đánh Giá Khả Năng Cho Vay")

# Nhập dữ liệu
STV = st.number_input("Nhập số tiền muốn vay (triệu đồng)", min_value=0.0)
TGV = st.number_input("Nhập thời gian vay (số năm)", min_value=0.0)
LSV = st.number_input("Nhập lãi suất cho vay (số thập phân, ví dụ 0.12)", min_value=0.0)
TN = st.number_input("Nhập thu nhập hàng tháng (triệu đồng/tháng)", min_value=0.0)
SNTGD = st.number_input("Nhập số người trong gia đình", min_value=0.0)
PTMC = st.number_input("Nhập số tiền phải trả cho khoản vay cũ (triệu đồng)", min_value=0.0)
GTTSDB = st.number_input("Nhập giá trị tài sản đảm bảo (triệu đồng)", min_value=0.0)
STKKH = st.number_input("Nhập số tuổi khách hàng", min_value=0)

CPSH = 5  # Chi phí sinh hoạt cố định

if st.button("Đánh giá khoản vay"):
    try:
        PTMM = (STV / (TGV * 12)) + (STV * (LSV / 12))
        DTI = (PTMC + PTMM) / (TN - SNTGD * CPSH)
        LTV = STV / GTTSDB

        st.write(f"**Chỉ số DTI:** {DTI * 100:.2f}%")
        st.write(f"**Chỉ số LTV:** {LTV * 100:.2f}%")

        if DTI <= 0.7 and LTV <= 0.7 and 18 <= STKKH <= 70:
            st.success("ĐƯỢC CHO VAY")
        else:
            st.error("KHÔNG ĐƯỢC CHO VAY")

    except ZeroDivisionError:
        st.warning("Vui lòng kiểm tra lại dữ liệu nhập, không được để giá trị mẫu số bằng 0.")
