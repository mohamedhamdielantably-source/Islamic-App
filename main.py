import streamlit as st
import google.generativeai as genai

# 1. إعداد مفتاح الـ API من الـ Secrets
# تأكد أنك وضعت API_KEY في إعدادات Streamlit -> Secrets
try:
    API_KEY = st.secrets["API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception as e:
    st.error("لم يتم العثور على مفتاح الـ API. تأكد من إضافته في إعدادات Secrets.")
    st.stop()

# 2. إعداد واجهة التطبيق
st.title("تطبيق إسلامي ذكي")
st.write("اسألني عن أي شيء في الدين وسأجيبك بفضل الله.")

# 3. صندوق المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. استقبال سؤال المستخدم
if prompt := st.chat_input("اكتب سؤالك هنا..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 5. الرد باستخدام Gemini
    with st.chat_message("assistant"):
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
