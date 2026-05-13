import streamlit as st

st.set_page_config(page_title="MBTI 영화·책 추천", page_icon="🎬")

st.title("🎬 MBTI 영화·책 추천 앱")
st.write("MBTI를 선택하면 어울리는 영화와 책을 추천해줍니다!")

mbti_data = {
    "INTJ": {
        "movie": {
            "title": "인터스텔라",
            "year": "2014",
            "price": "약 14,000원",
            "feature": "깊은 사고와 전략적인 성격을 가진 INTJ에게 어울리는 SF 영화"
        },
        "book": {
            "title": "사피엔스",
            "year": "2011",
            "price": "약 22,000원",
            "feature": "인류의 역사와 미래를 분석적으로 설명하는 책"
        }
    },
    "INTP": {
        "movie": {
            "title": "매트릭스",
            "year": "1999",
            "price": "약 12,000원",
            "feature": "논리적이고 철학적인 질문을 좋아하는 INTP에게 추천"
        },
        "book": {
            "title": "코스모스",
            "year": "1980",
            "price": "약 19,000원",
            "feature": "우주와 과학에 대한 호기심을 자극하는 책"
        }
    },
    "ENTJ": {
        "movie": {
            "title": "아이언맨",
            "year": "2008",
            "price": "약 13,000원",
            "feature": "리더십과 추진력이 강한 ENTJ와 잘 어울리는 영화"
        },
        "book": {
            "title": "원씽",
            "year": "2013",
            "price": "약 16,000원",
            "feature": "목표 달성과 집중력을 강조하는 자기계발서"
        }
    },
    "ENTP": {
        "movie": {
            "title": "인셉션",
            "year": "2010",
            "price": "약 14,000원",
            "feature": "창의적이고 아이디어가 많은 ENTP에게 추천"
        },
        "book": {
            "title": "멋진 신세계",
            "year": "1932",
            "price": "약 13,000원",
            "feature": "새로운 관점과 상상력을 자극하는 소설"
        }
    },
    "INFJ": {
        "movie": {
            "title": "죽은 시인의 사회",
            "year": "1989",
            "price": "약 11,000원",
            "feature": "이상과 가치관을 중요하게 생각하는 INFJ에게 추천"
        },
        "book": {
            "title": "어린 왕자",
            "year": "1943",
            "price": "약 10,000원",
            "feature": "따뜻한 감성과 철학적 메시지가 담긴 책"
        }
    },
    "INFP": {
        "movie": {
            "title": "월터의 상상은 현실이 된다",
            "year": "2013",
            "price": "약 12,000원",
            "feature": "상상력과 감성이 풍부한 INFP에게 어울리는 영화"
        },
        "book": {
            "title": "연금술사",
            "year": "1988",
            "price": "약 14,000원",
            "feature": "꿈과 성장 이야기를 담은 감성 소설"
        }
    },
    "ENFJ": {
        "movie": {
            "title": "굿 윌 헌팅",
            "year": "1997",
            "price": "약 11,000원",
            "feature": "사람의 성장과 관계를 중요하게 생각하는 ENFJ에게 추천"
        },
        "book": {
            "title": "미움받을 용기",
            "year": "2013",
            "price": "약 15,000원",
            "feature": "인간관계와 삶의 태도에 대한 통찰을 주는 책"
        }
    },
    "ENFP": {
        "movie": {
            "title": "라라랜드",
            "year": "2016",
            "price": "약 13,000원",
            "feature": "열정적이고 자유로운 ENFP에게 어울리는 영화"
        },
        "book": {
            "title": "데미안",
            "year": "1919",
            "price": "약 9,000원",
            "feature": "자아 탐색과 성장 이야기를 담은 소설"
        }
    },
    "ISTJ": {
        "movie": {
            "title": "포레스트 검프",
            "year": "1994",
            "price": "약 12,000원",
            "feature": "성실함과 책임감을 중요하게 여기는 ISTJ에게 추천"
        },
        "book": {
            "title": "아주 작은 습관의 힘",
            "year": "2018",
            "price": "약 16,000원",
            "feature": "꾸준함과 실천의 중요성을 알려주는 책"
        }
    },
    "ISFJ": {
        "movie": {
            "title": "코코",
            "year": "2017",
            "price": "약 13,000원",
            "feature": "따뜻한 가족애와 배려심이 담긴 영화"
        },
        "book": {
            "title": "나미야 잡화점의 기적",
            "year": "2012",
            "price": "약 15,000원",
            "feature": "사람 사이의 따뜻한 이야기를 담은 소설"
        }
    },
    "ESTJ": {
        "movie": {
            "title": "머니볼",
            "year": "2011",
            "price": "약 12,000원",
            "feature": "체계적이고 현실적인 ESTJ에게 추천"
        },
        "book": {
            "title": "성공하는 사람들의 7가지 습관",
            "year": "1989",
            "price": "약 18,000원",
            "feature": "효율성과 리더십을 강조하는 책"
        }
    },
    "ESFJ": {
        "movie": {
            "title": "인사이드 아웃",
            "year": "2015",
            "price": "약 13,000원",
            "feature": "감정과 공감을 중요하게 여기는 ESFJ에게 추천"
        },
        "book": {
            "title": "아몬드",
            "year": "2017",
            "price": "약 14,000원",
            "feature": "감정과 관계를 따뜻하게 풀어낸 소설"
        }
    },
    "ISTP": {
        "movie": {
            "title": "탑건: 매버릭",
            "year": "2022",
            "price": "약 15,000원",
            "feature": "도전적이고 현실 감각이 뛰어난 ISTP에게 추천"
        },
        "book": {
            "title": "팩트풀니스",
            "year": "2018",
            "price": "약 18,000원",
            "feature": "사실 기반 사고를 키워주는 책"
        }
    },
    "ISFP": {
        "movie": {
            "title": "업",
            "year": "2009",
            "price": "약 11,000원",
            "feature": "감성적이고 따뜻한 ISFP에게 잘 어울리는 영화"
        },
        "book": {
            "title": "모모",
            "year": "1973",
            "price": "약 12,000원",
            "feature": "삶의 소중함을 느끼게 하는 판타지 소설"
        }
    },
    "ESTP": {
        "movie": {
            "title": "분노의 질주",
            "year": "2001",
            "price": "약 12,000원",
            "feature": "에너지 넘치고 활동적인 ESTP에게 추천"
        },
        "book": {
            "title": "넛지",
            "year": "2008",
            "price": "약 17,000원",
            "feature": "실생활 심리학과 행동경제학을 다룬 책"
        }
    },
    "ESFP": {
        "movie": {
            "title": "위대한 쇼맨",
            "year": "2017",
            "price": "약 14,000원",
            "feature": "즐거움과 열정을 사랑하는 ESFP에게 추천"
        },
        "book": {
            "title": "트렌드 코리아",
            "year": "2025",
            "price": "약 19,000원",
            "feature": "최신 트렌드와 사회 변화를 흥미롭게 설명하는 책"
        }
    }
}

mbti = st.selectbox(
    "MBTI를 선택하세요",
    list(mbti_data.keys())
)

if mbti:
    data = mbti_data[mbti]

    st.header(f"✨ {mbti} 추천 결과")

    st.subheader("🎬 영화 추천")
    st.write(f"제목: {data['movie']['title']}")
    st.write(f"연도: {data['movie']['year']}")
    st.write(f"가격: {data['movie']['price']}")
    st.write(f"특징: {data['movie']['feature']}")

    st.subheader("📚 책 추천")
    st.write(f"제목: {data['book']['title']}")
    st.write(f"연도: {data['book']['year']}")
    st.write(f"가격: {data['book']['price']}")
    st.write(f"특징: {data['book']['feature']}")

st.markdown("---")
st.caption("Streamlit Cloud에서 바로 실행 가능한 MBTI 추천 ")
