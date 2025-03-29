import streamlit as st
from llm_loader import load_llm
from data_loader import load_all_documents_from_folder
from rag_engine import create_qa_chain

st.set_page_config(page_title="📁 Folder RAG Chat", layout="wide")
st.title("📁 ChatGPT + 多格式資料夾問答系統")

# Sidebar
openai_api_key = st.sidebar.text_input("🔑 請輸入 OpenAI API Key", type="password")
llm_provider = st.sidebar.selectbox("🧠 選擇 LLM 提供者", ["openai"])
llm_model = st.sidebar.selectbox("📦 選擇模型", ["gpt-3.5-turbo", "gpt-4-turbo"])

# 🔽 主介面輸入資料夾路徑 & 問題
st.markdown("### 📂 請輸入你想處理的資料夾路徑")
folder_path = st.text_input("範例：`./my_docs` 或 `D:/files/chatpdf/`")

if openai_api_key:
    st.success("✅ 資料夾與 API Key 已就緒！")
    user_question = st.text_input("💬 請輸入你的問題")

    if user_question:
        with st.spinner("🔍 正在處理..."):
            docs = load_all_documents_from_folder(folder_path)
            llm = load_llm(provider=llm_provider, model_name=llm_model, api_key=openai_api_key)
            qa_chain = create_qa_chain(docs, llm, openai_api_key)
            result = qa_chain(user_question)

            st.markdown("### 🧠 回答內容")
            st.write(result["result"])

            st.markdown("### 📄 引用段落")
            for i, doc in enumerate(result["source_documents"]):
                with st.expander(f"來源 {i+1}: {doc.metadata['source']}"):
                    st.write(doc.page_content)
else:
    st.info("請輸入 API 金鑰與資料夾路徑。")
