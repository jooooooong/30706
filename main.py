import streamlit as st
import pandas as pd
import plotly.express as px

# 웹앱 제목
st.title("CSV 데이터 시각화 웹앱")

# 데이터 불러오기
@st.cache_data
def load_data():
    url = 'https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY'
    df = pd.read_csv(url)
    return df

df = load_data()

# 데이터 프리뷰
st.subheader("데이터 미리보기")
st.write(df.head())

# 열 선택
columns = df.columns.tolist()
selected_column = st.selectbox("시각화할 열을 선택하세요:", columns)

# 그래프 타입 선택
chart_type = st.radio("차트 종류 선택:", ["히스토그램", "라인 차트", "박스 플롯"])

# 차트 생성
st.subheader(f"'{selected_column}' 컬럼의 {chart_type}")
if chart_type == "히스토그램":
    fig = px.histogram(df, x=selected_column)
elif chart_type == "라인 차트":
    fig = px.line(df, y=selected_column)
elif chart_type == "박스 플롯":
    fig = px.box(df, y=selected_column)

st.plotly_chart(fig)
