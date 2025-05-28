import streamlit as st
import pandas as pd
import plotly.express as px

# Streamlit 앱 제목
st.set_page_config(page_title="데이터 시각화 앱", layout="wide")
st.title("📊 구글 드라이브 데이터 Plotly 시각화")

# 데이터 URL (구글 드라이브 공유 링크)
data_url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"

@st.cache_data
def load_data():
    try:
        df = pd.read_csv(data_url)
        return df
    except Exception as e:
        st.error(f"데이터를 불러오는 중 오류 발생: {e}")
        return pd.DataFrame()

# 데이터 불러오기
df = load_data()

if not df.empty:
    st.subheader("데이터 미리보기")
    st.dataframe(df)

    # 컬럼 선택
    st.subheader("📈 시각화")
    columns = df.columns.tolist()
    x_axis = st.selectbox("X축 선택", columns)
    y_axis = st.selectbox("Y축 선택", columns, index=1 if len(columns) > 1 else 0)
    chart_type = st.selectbox("차트 유형 선택", ["산점도 (scatter)", "라인 (line)", "바 (bar)"])

    # Plotly 시각화
    fig = None
    if chart_type == "산점도 (scatter)":
        fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
    elif chart_type == "라인 (line)":
        fig = px.line(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
    elif chart_type == "바 (bar)":
        fig = px.bar(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")

    if fig:
        st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("데이터를 불러올 수 없습니다. 링크나 파일 형식을 확인해주세요.")
