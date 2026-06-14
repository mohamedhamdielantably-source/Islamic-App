import streamlit as st
import google.generativeai as genai

# إعداد الـ API
if "API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("خطأ: مفتاح الـ API غير موجود في الـ Secrets.")
    st.stop()

st.title("تطبيق إسلامي ذكي 🕌")
st.write("أهلاً يا زهرة، اسأليني أي سؤال وسأجيبك.")

# تهيئة الشات
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# إرسال الرسالة
if prompt := st.chat_input("اكتب سؤالك هنا..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # الرد باسمك
        full_prompt = f"أنت مساعد إسلامي ذكي، صممك البشمهندس محمد حمدي. السؤال هو: {prompt}"
        response = model.generate_content(full_prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
