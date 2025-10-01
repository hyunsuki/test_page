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
    .segmented-wrapper {{
        display: flex;
        justify-content: center;
        width: 100%;
        margin: 20px 0;
    }}
    .segmented-control {{
        display: flex;
        border-radius: 30px;
        background-color: #f5f5f5;
        padding: 4px;
        width: 60%; /* 토글 전체 폭 (원하는 비율로 조정) */
        max-width: 600px;
        min-width: 300px;
    }}
    .segment {{
        flex: 1;  /* 균등 분할 */
        text-align: center;
        padding: 10px 0;
        border-radius: 25px;
        cursor: pointer;
        font-weight: 600;
        font-size: 16px;
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

    <div class="segmented-wrapper">
        <div class="segmented-control">
            {"".join([
                f"<div class='segment {'selected' if st.session_state.selected == opt else ''}' onclick=\"window.parent.postMessage({{'type': 'streamlit_set', 'key': 'selected', 'value': '{opt}'}}, '*')\">{opt}</div>"
                for opt in options
            ])}
        </div>
    </div>
""", unsafe_allow_html=True)
