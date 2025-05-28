plotly

import streamlit as st
import pandas as pd
import plotly.express as px

# --- 웹 앱 제목 설정 ---
st.set_page_config(layout="wide") # 페이지 레이아웃을 넓게 설정
st.title('📊 Google Drive 데이터 Plotly 시각화 웹 앱')
st.markdown("---") # 구분선 추가

# --- Google Drive 데이터 링크 ---
# 이 링크는 직접 다운로드 가능한 CSV 파일 링크여야 합니다.
# Google Drive에서 '링크가 있는 모든 사용자에게 공개'로 설정해야 합니다.
GOOGLE_DRIVE_URL = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPFiofYlni0HVVY"

# --- 데이터 로드 함수 (캐싱 적용) ---
@st.cache_data # 데이터를 한번 로드하면 다시 로드하지 않도록 캐싱하여 성능 최적화
def load_data(url):
    """
    지정된 URL에서 데이터를 로드합니다.
    """
    try:
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"⚠️ 데이터를 로드하는 데 실패했습니다. 오류: {e}")
        st.error("💡 **Google Drive 링크가 올바른지, 그리고 파일 접근 권한이 '링크가 있는 모든 사용자에게 공개'로 설정되어 있는지 확인해주세요.**")
        return None

# --- 데이터 로드 및 확인 ---
df = load_data(GOOGLE_DRIVE_URL)

if df is not None:
    st.success("✅ 데이터 로드 성공!")
    st.write("### 📋 로드된 데이터 미리보기")
    st.dataframe(df.head()) # 데이터프레임의 상위 5행을 보여줍니다.
    st.write(f"총 {df.shape[0]} 행, {df.shape[1]} 열")
    st.markdown("---")

    st.write("### 📈 데이터 시각화")

    # 데이터의 모든 컬럼 목록을 가져옵니다.
    all_columns = df.columns.tolist()

    # 시각화할 컬럼이 충분한지 확인
    if len(all_columns) >= 2:
        # 사용자에게 X축과 Y축 컬럼을 선택할 수 있도록 드롭다운 메뉴 제공
        col1, col2 = st.columns(2) # 두 개의 컬럼으로 레이아웃 분할

        with col1:
            x_axis = st.selectbox('X축으로 사용할 컬럼을 선택해주세요', all_columns, help="X축에 표시될 데이터 컬럼을 선택합니다.")
        with col2:
            # Y축 선택 시 X축으로 선택된 컬럼을 제외
            y_axis = st.selectbox('Y축으로 사용할 컬럼을 선택해주세요', [col for col in all_columns if col != x_axis], help="Y축에 표시될 데이터 컬럼을 선택합니다.")

        # Plotly 그래프 생성 버튼
        if st.button('✨ 그래프 그리기', help="선택된 컬럼으로 시각화를 생성합니다."):
            if x_axis and y_axis: # 두 축이 모두 선택되었는지 확인
                try:
                    # 선택된 컬럼으로 꺾은선 그래프 생성 (가장 일반적인 경우)
                    # 데이터의 종류에 따라 px.scatter, px.bar 등 다른 함수를 사용할 수 있습니다.
                    fig = px.line(df, x=x_axis, y=y_axis,
                                  title=f'**{y_axis}** vs **{x_axis}** 시각화',
                                  labels={x_axis: f'**{x_axis}**', y_axis: f'**{y_axis}**'},
                                  template="plotly_white") # 그래프 테마 설정

                    # 그래프 레이아웃 커스터마이징 (선택 사항)
                    fig.update_layout(
                        title_font_size=24,
                        xaxis_title_font_size=18,
                        yaxis_title_font_size=18,
                        hovermode="x unified" # 마우스 오버 시 정보 표시 방식
                    )

                    # Streamlit에 Plotly 그래프 표시
                    st.plotly_chart(fig, use_container_width=True) # 컨테이너 너비에 맞춰 그래프 크기 조절
                    st.success("🎉 그래프가 성공적으로 생성되었습니다!")

                except Exception as e:
                    st.error(f"❌ 그래프를 그리는 데 실패했습니다. 오류: {e}")
                    st.error("💡 **선택된 컬럼의 데이터 타입이 시각화에 적합한지 확인해주세요.** (예: 숫자가 아닌 컬럼을 Y축으로 선택했는지)")
            else:
                st.warning("⚠️ X축과 Y축 컬럼을 모두 선택해주세요.")
    else:
        st.warning("⚠️ 데이터를 시각화할 수 있는 충분한 컬럼(최소 2개)이 없습니다.")
        st.info(f"현재 데이터의 모든 컬럼: `{', '.join(all_columns)}`")

else:
    st.info("⬆️ 데이터를 로드할 수 없어 시각화를 진행할 수 없습니다. 위의 오류 메시지를 확인해주세요.")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit & Plotly")
