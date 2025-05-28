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
    st.subheader("📊 기본 막대 그래프 시각화")

    # 컬럼 선택
    columns = df.columns.tolist()
    x_axis = st.selectbox("X축 선택", columns)
    y_axis = st.selectbox("Y축 선택", columns, index=1 if len(columns) > 1 else 0)

    # Plotly 막대 그래프
    fig = px.bar(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")

    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("⬆️ 데이터를 로드할 수 없어 시각화를 진행할 수 없습니다. 위의 오류 메시지를 확인해주세요.")
