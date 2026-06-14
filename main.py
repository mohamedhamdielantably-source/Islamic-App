import streamlit as st

st.set_page_config(page_title="تطبيقي الإسلامي", page_icon="🕌")
st.title("تطبيق إسلامي ذكي 🕌")
st.write("أهلاً بك! أنا هنا للإجابة على أسئلتك الدينية.")

# قاعدة بيانات الأسئلة والأجوبة (تقدر تضيف فيها اللي إنت عايزه)
data = {
    "أركان الإسلام": "أركان الإسلام خمسة: شهادة أن لا إله إلا الله وأن محمداً رسول الله، إقام الصلاة، إيتاء الزكاة، صوم رمضان، وحج البيت لمن استطاع إليه سبيلاً.",
    "من صممك": "لقد صممني البشمهندس محمد حمدي، المبرمج المبدع.",
    "كيف أتوب": "التوبة هي الرجوع إلى الله، وشروطها: الإقلاع عن الذنب، الندم عليه، والعزم على عدم العودة."
}

# الشات
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("اكتب سؤالك (مثلاً: أركان الإسلام):"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # الرد من قاعدة البيانات
        response_text = data.get(prompt, "عذراً، أنا حالياً أجيب عن الأسئلة المبرمجة فقط. سأتعلم المزيد قريباً!")
        st.markdown(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})
