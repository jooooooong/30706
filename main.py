import streamlit as st
import pandas as pd
import plotly.express as px

# Streamlit 앱 제목
st.set_page_config(page_title="데이터 시각화 앱", layout="wide")
st.title("📊 구글 드라이브 데이터 Plotly 시각화")

# Google Drive 공유 링크 (반드시 공개 권한으로!)
data_url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

@st.cache_data
def load_data():
    try:
        df = pd.read_csv(data_url)
        return df
    except Exception as e:
        st.error(f"⚠️ 데이터를 로드하는 데 실패했습니다. 오류: {e}")
        return pd.DataFrame()

# 데이터 불러오기
df = load_data()

if not df.empty:
    st.subheader("데이터 미리보기")
