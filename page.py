# this is test page

import streamlit as st
import pandas as pd

# ─────────────────────────────────────────────
# Streamlit UI
# ─────────────────────────────────────────────

st.set_page_config(page_title="다이렉트 굿앤굿어린이종합보험Q(태아)", layout="wide")

# 옵션 정의
options = ["태아", "어린이 (0~15세)"]

# 기본 radio 컴포넌트 (라벨은 숨김 처리 예정)
choice = st.radio(
    "선택", 
    options, 
    horizontal=True,
    label_visibility="collapsed"
)

# CSS로 디자인 커스터마이징
st.markdown("""
    <style>
    /* radio 전체 영역 */
    div[data-baseweb="radio"] {
        display: flex;
        justify-content: flex-start;
        background-color: #f5f5f5;
        padding: 4px;
        border-radius: 25px;
        width: fit-content;
    }

    /* 개별 옵션 버튼 */
    div[data-baseweb="radio"] > div {
        flex: 1;
    }

    div[data-baseweb="radio"] label {
        background: transparent;
        padding: 6px 18px;
        border-radius: 20px;
        font-weight: 600;
        color: #666;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    /* 선택된 옵션 */
    div[data-baseweb="radio"] input:checked + div {
        background: white;
        color: black;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.15);
        border-radius: 20px;
    }

    /* 기본 input 숨기기 */
    div[data-baseweb="radio"] input {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# 선택 값 활용
st.write("👉 선택된 값:", choice)
