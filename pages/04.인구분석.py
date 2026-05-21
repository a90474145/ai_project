import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

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
df = pd.read_csv("population.csv", encoding="utf-8")

# -----------------------------
# 필요한 데이터 추출
# -----------------------------
# 행정구 이름 컬럼
district_col = df.columns[0]

# 숫자 데이터만 추출
numeric_df = df.select_dtypes(include='number')

# 연령 데이터 컬럼 찾기
age_columns = []

for col in numeric_df.columns:
    col_str = str(col)

    # 나이 관련 컬럼만 추출
    if '세' in col_str or '연령' in col_str:
        age_columns.append(col)

# -----------------------------
# 행정구 선택
# -----------------------------
districts = df[district_col].tolist()

selected_district = st.selectbox(
    "행정구를 선택하세요",
    districts
)

# 선택한 행정구 데이터
selected_row = df[df[district_col] == selected_district]

# -----------------------------
# 그래프 데이터 준비
# -----------------------------
ages = []
population = []

for col in age_columns:
    try:
        ages.append(str(col))
        population.append(int(selected_row[col].values[0]))
    except:
        pass

# -----------------------------
# 그래프 그리기
# -----------------------------
fig, ax = plt.subplots(figsize=(14, 6))

# 회색 배경
fig.patch.set_facecolor('lightgray')
ax.set_facecolor('lightgray')

# 빨간색 꺾은선 그래프
ax.plot(
    ages,
    population,
    color='red',
    linewidth=2,
    marker='o'
)

# 제목 및 축 설정
ax.set_title("서울시 행정구별 인구수", fontsize=18)
ax.set_xlabel("나이", fontsize=12)
ax.set_ylabel("인구수", fontsize=12)

# x축 글자 회전
plt.xticks(rotation=90)

# 여백 자동 조정
plt.tight_layout()

# 그래프 출력
st.pyplot(fig)
