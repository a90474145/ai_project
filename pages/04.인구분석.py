import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(page_title="서울시 행정구별 인구수", layout="wide")

st.title("서울시 행정구별 인구수")

# -----------------------------
# 한글 폰트 설정
# -----------------------------
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# -----------------------------
# 데이터 불러오기
# -----------------------------
df = pd.read_csv("population.csv", encoding="cp949")

# -----------------------------
# 행정구 컬럼
# -----------------------------
district_col = df.columns[0]

# -----------------------------
# 연령 컬럼 찾기
# -----------------------------
age_columns = []

for col in df.columns:
    col_str = str(col)

    if "세" in col_str:
        age_columns.append(col)

# -----------------------------
# 행정구 선택
# -----------------------------
districts = df[district_col].tolist()

selected_district = st.selectbox(
    "행정구를 선택하세요",
    districts
)

# 선택 데이터
selected_row = df[df[district_col] == selected_district]

# -----------------------------
# 그래프 데이터 준비
# -----------------------------
ages = []
population = []

for col in age_columns:
    try:
        value = str(selected_row[col].values[0]).replace(",", "")

        ages.append(col)
        population.append(int(value))

    except:
        pass

# -----------------------------
# 그래프 그리기
# -----------------------------
fig, ax = plt.subplots(figsize=(14, 6))

# 회색 배경
fig.patch.set_facecolor("lightgray")
ax.set_facecolor("lightgray")

# 빨간색 꺾은선 그래프
ax.plot(
    ages,
    population,
    color="red",
    linewidth=2,
    marker="o"
)

# 제목 및 축
ax.set_title("서울시 행정구별 인구수", fontsize=18)
ax.set_xlabel("나이", fontsize=12)
ax.set_ylabel("인구수", fontsize=12)

# x축 회전
plt.xticks(rotation=90)

# 레이아웃 정리
plt.tight_layout()

# 출력
st.pyplot(fig)
