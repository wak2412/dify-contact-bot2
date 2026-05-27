import streamlit as st
import requests

# =========================
# Dify設定
# =========================

API_KEY = "ここにDifyのAPIキー"

URL = "https://api.dify.ai/v1/chat-messages"

# =========================
# 画面タイトル
# =========================

st.title("問い合わせBot")

# =========================
# モード選択
# =========================

mode = st.selectbox(
    "モード選択",
    [
        "メール作成モード",
        "メール添削モード",
        "質問回答モード"
    ]
)

query = ""

# =========================
# メール作成モード
# =========================

if mode == "メール作成モード":

    inquiry = st.text_area("お問い合わせ内容")

    history = st.text_area("過去のやり取り（任意）")

    query = f"""
    【モード】
    メール作成モード

    【お問い合わせ内容】
    {inquiry}

    【過去のやり取り】
    {history}
    """

# =========================
# メール添削モード
# =========================

elif mode == "メール添削モード":

    mail = st.text_area("添削対象メール")

    direction = st.text_input("添削の方向性")

    query = f"""
    【モード】
    メール添削モード

    【添削対象メール】
    {mail}

    【添削の方向性】
    {direction}
    """

# =========================
# 質問回答モード
# =========================

elif mode == "質問回答モード":

    question = st.text_area("質問したい内容")

    query = f"""
    【モード】
    質問回答モード

    【質問内容】
    {question}
    """

# =========================
# 送信ボタン
# =========================

if st.button("送信"):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "inputs": {},
        "query": query,
        "response_mode": "blocking",
        "user": "user123"
    }

    response = requests.post(
        URL,
        headers=headers,
        json=data
    )

    result = response.json()

    # =========================
    # 回答表示
    # =========================

    if "answer" in result:
        st.write(result["answer"])
    else:
        st.error(result)
