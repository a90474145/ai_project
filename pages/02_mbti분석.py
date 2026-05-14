import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# 페이지 설정
st.set_page_config(
    page_title="국가별 MBTI 분석",
    page_icon="🌍",
    layout="wide"
)

# 제목
st.title("🌍 국가별 MBTI 비율 분석")
st.markdown("국가를 선택하면 MBTI 비율을 인터랙티브하게 확인할 수 있습니다.")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# 국가 선택
countries = sorted(df["Country"].unique())

selected_country = st.selectbox(
    "국가를 선택하세요",
    countries
)

# 선택한 국가 데이터
country_data = df[df["Country"] == selected_country].iloc[0]

# MBTI 데이터 추출
mbti_columns = df.columns[1:]

mbti_values = pd.DataFrame({
    "MBTI": mbti_columns,
    "Ratio": [country_data[col] for col in mbti_columns]
})

# 비율 내림차순 정렬
mbti_values = mbti_values.sort_values(
    by="Ratio",
    ascending=False
).reset_index(drop=True)

# 1등 MBTI 찾기
top_mbti = mbti_values.iloc[0]["MBTI"]

# 색상 지정
colors = []

blue_gradient = px.colors.sequential.Blues[::-1]

for i, row in mbti_values.iterrows():
    if row["MBTI"] == top_mbti:
        colors.append("red")
    else:
        gradient_index = min(i, len(blue_gradient) - 1)
        colors.append(blue_gradient[gradient_index])

# Plotly 그래프
fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=mbti_values["MBTI"],
        y=mbti_values["Ratio"],
        marker_color=colors,
        text=[
            f"{v*100:.2f}%"
            for v in mbti_values["Ratio"]
        ],
        textposition="outside",
        hovertemplate=
        "<b>%{x}</b><br>" +
        "비율: %{y:.2%}<extra></extra>"
    )
)

# 레이아웃 설정
fig.update_layout(
    title=f"{selected_country}의 MBTI 비율",
    xaxis_title="MBTI 유형",
    yaxis_title="비율",
    template="plotly_white",
    height=650,
    hovermode="x unified",
    font=dict(size=14),
    title_font=dict(size=24),
    xaxis=dict(
        tickangle=-20
    ),
    yaxis=dict(
        tickformat=".0%"
    )
)

# 그래프 출력
st.plotly_chart(fig, use_container_width=True)

# 상위 MBTI 표시
st.subheader("🏆 가장 높은 MBTI")

st.success(
    f"{selected_country}에서 가장 높은 유형은 "
    f"'{top_mbti}' "
    f"({mbti_values.iloc[0]['Ratio']*100:.2f}%) 입니다."
)

# 데이터 테이블
with st.expander("📄 데이터 보기"):
    st.dataframe(
        mbti_values,
        use_container_width=True
    )
