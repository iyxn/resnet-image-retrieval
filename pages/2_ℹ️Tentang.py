import streamlit as st

st.set_page_config(
    page_title="Dashboard Forecasting", layout="wide")



col1, col2 = st.columns(2)

with col1:
    st.subheader("\t\t\t\t\tHardian Alkori")
    url1 = "https://id.linkedin.com/in/hardian-alkori-029017249"
    url2 = "https://github.com/hardianalkori"
    st.write("With my knowledge of machine learning algorithms and data analytics allows me to build outstanding stuff with it. So, what can i do for you?")
    st.write("Reach me on [LinkedIn](%s) | Follow me on [GitHub](%s)" % (url1, url2))



