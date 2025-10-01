# this is test page

import streamlit as st
import pandas as pd

# ─────────────────────────────────────────────
# Streamlit UI
# ─────────────────────────────────────────────

st.set_page_config(page_title="다이렉트 굿앤굿어린이종합보험Q(태아)", layout="wide")

# 초기 상태 저장
if "selected" not in st.session_state:
    st.session_state.selected = "태아"

# 옵션 정의
options = ["태아", "어린이 (0~15세)"]

# CSS + HTML 커스텀 토글 UI
st.markdown(f"""
    <style>
    .segmented-control {{
        display: inline-flex;
        border-radius: 25px;
        background-color: #f5f5f5;
        padding: 4px;
    }}
    .segment {{
        padding: 8px 20px;
        border-radius: 20px;
        margin: 0 2px;
        cursor: pointer;
        font-weight: 600;
        color: #666;
        background-color: transparent;
        transition: all 0.3s ease;
    }}
    .segment.selected {{
        background-color: white;
        color: black;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.15);
    }}
    </style>

    <div class="segmented-control">
        {"".join([
            f"<div class='segment {'selected' if st.session_state.selected == opt else ''}' onclick=\"window.parent.postMessage({{'type': 'streamlit_set', 'key': 'selected', 'value': '{opt}'}}, '*')\">{opt}</div>"
            for opt in options
        ])}
    </div>
""", unsafe_allow_html=True)

# 선택 값 확인 (테스트용)
#st.write("현재 선택:", st.session_state.selected)
