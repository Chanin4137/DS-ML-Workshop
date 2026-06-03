import streamlit as st

st.set_page_config(page_title="MyApp", layout="wide")

st.title("🏠 หน้าหลัก ")
st.write("### Boot Camp: Data Science and Machine Learning")
st.info("7 Day Intensive Hands-on Workshop")
st.markdown(''':rainbow[VoVoVoVoVoVoVoVoVoVoVoVoVoVoVoVoVoVoVoVoVoVoVoVoVoVoVoVoVoVo]''')
if st.button("💰 ระบบคำนวณส่วนลดตามยอดซื้อ"):
    st.switch_page("pages/app1_discount_calc.py")
elif st.button("🧼 Customer Data Cleaner"):
    st.switch_page("pages/clean_customers.py")
elif st.button("⚒️ Mini Project"):
    st.switch_page("pages/energy_inventory.py")
elif st.button("🧹 clean app"):
    st.switch_page("pages/clean_app.py")
elif st.button("🪅 clean app by ชานอิน"):
    st.switch_page("pages/clean_app_by_chanin.py")
elif st.button("😋 Transformer APP by ชานอิน"):
    st.switch_page("pages/transform_app.py")
