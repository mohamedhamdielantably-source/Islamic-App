import streamlit as st
import google.generativeai as genai

# إعداد مفتاح الـ API
try:
    API_KEY = st.secrets["API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception as e:
    st.error("خطأ: لم يتم العثور على مفتاح الـ API في إعدادات Secrets.")
    st.stop()

st.title("تطبيق إسلامي ذكي 🕌")
st.write("أهلاً بك! اسألني عن أي شيء في الدين وسأجيبك بفضل الله.")

# تهيئة سجل المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# استقبال سؤال المستخدم
if prompt := st.chat_input("اكتب سؤالك هنا..."):
    # إضافة سؤال المستخدم للسجل
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # توليد الرد باستخدام Gemini
    with st.chat_message("assistant"):
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            full_response = response.text
            st.markdown(full_response)
            # إضافة رد المساعد للسجل
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            st.error("حدث خطأ أثناء التواصل مع الذكاء الاصطناعي.")
