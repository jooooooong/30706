📁 your-project/
├── main.py
└── requirements.txt
import streamlit as st
import pandas as pd
import plotly.express as px

# 제목
st.title("📊 Google Drive CSV 시각화")

# 데이터 URL
url = 'https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY'

# 데이터 불러오기
@st.cache_data
def load_data():
    return pd.read_csv(url)

try:
    df = load_data()
    st.success("✅ 데이터 로드 완료!")

    st.write("데이터 미리보기:")
    st.dataframe(df.head())

    # Plotly 시각화
    st.subheader("📈 Plotly 시각화")
    
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    if len(numeric_cols) < 2:
        st.warning("⚠️ 시각화를 위한 숫자형 컬럼이 충분하지 않습니다.")
    else:
        x_axis = st.selectbox("X축 선택", numeric_cols)
        y_axis = st.selectbox("Y축 선택", numeric_cols, index=1)

        fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
        st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"⚠️ 데이터를 로드하는 데 실패했습니다.\n\n오류: {e}")
streamlit
pandas
plotly
