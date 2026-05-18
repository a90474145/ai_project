import streamlit as st
import folium
from streamlit.components.v1 import html

st.set_page_config(page_title="서울 관광지", layout="wide")

st.title("🇰🇷 외국인이 좋아하는 서울 관광지 TOP10")

places = [
    {
        "name": "경복궁",
        "lat": 37.579617,
        "lon": 126.977041,
        "subway": "경복궁역(3호선)",
        "fun": "한복체험, 북촌한옥마을"
    },
    {
        "name": "명동",
        "lat": 37.563757,
        "lon": 126.982193,
        "subway": "명동역(4호선)",
        "fun": "쇼핑, 길거리 음식"
    },
    {
        "name": "홍대",
        "lat": 37.556336,
        "lon": 126.922031,
        "subway": "홍대입구역(2호선)",
        "fun": "버스킹, 맛집 탐방"
    },
    {
        "name": "강남",
        "lat": 37.497952,
        "lon": 127.027619,
        "subway": "강남역(2호선)",
        "fun": "카페, 쇼핑"
    },
    {
        "name": "N서울타워",
        "lat": 37.551169,
        "lon": 126.988227,
        "subway": "명동역(4호선)",
        "fun": "야경 감상, 케이블카"
    },
]

# 지도 생성
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11
)

# 마커 추가
for place in places:

    popup_text = f"""
    <b>{place['name']}</b><br>
    🚇 {place['subway']}<br>
    🎉 {place['fun']}
    """

    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=popup_text,
        tooltip=place["name"],
        icon=folium.Icon(color="red")
    ).add_to(m)

# 지도 HTML 렌더링
map_html = m._repr_html_()

html(map_html, height=600)

st.divider()

st.subheader("📍 관광지 정보")

for place in places:
    st.info(
        f"{place['name']} | 🚇 {place['subway']} | 🎉 {place['fun']}"
    )
